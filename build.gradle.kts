import org.apache.sshd.client.session.ClientSession
import org.apache.sshd.client.SshClient
import org.apache.sshd.scp.client.ScpClientCreator
import org.apache.sshd.scp.client.ScpClient
import java.nio.file.Files
import java.nio.file.Paths
import kotlin.collections.listOf
import kotlin.streams.toList

plugins {
    kotlin("jvm") version "1.5.31"
    id("ru.vyarus.use-python") version "3.0.0"
    id("io.github.DiLilloDaniele.gradle-python-testing") version "1.4.4"
    alias(libs.plugins.gitSemVer)
    alias(libs.plugins.kotlin.qa)
}

group = "org.IntelligentBackpack"
val flakeExcludeTypes = listOf<String>("E501")
val virtualEnvFolder = "$projectDir/.gradle/python"

repositories {
    mavenCentral()
}

buildscript {
    repositories {
        mavenCentral()
    }

    dependencies {
        "classpath"("org.apache.sshd:sshd-core:2.9.2")
        "classpath"("org.apache.sshd:sshd-scp:2.9.2")
    }
}

tasks.named("build").configure {
    dependsOn(tasks.named("pipInstall"))
}

python {
    pip("pdoc3:0.10.0")
    pip("tinydb:4.7.1")
    pip("coverage:7.2.2")
    // flake:5.0.4 or 6.0.0
    pip("flake8:5.0.4")
    pip("azure-iot-device:3.0.0b2")
    // pip("gpiozero:1.6.2")
    // pip("azure-servicebus:7.9.0")
    // pip("pi-rc522:2.2.1")
    minPythonVersion = "3.2"
    minPipVersion = "9.0.1"
    python.scope = ru.vyarus.gradle.plugin.python.PythonExtension.Scope.USER
}

pytest {
    testSrc.set("src/test")
    minCoveragePercValue.set(50)
    useVirtualEnv.set(true)
    virtualEnvFolder.set(".gradle/python")
}

tasks.register<Exec>("createVirtualEnv") {
    val directoryPath = "$projectDir/.gradle/python"
    val file = File(directoryPath)
    doLast {
        if (!file.isDirectory) {
            commandLine("python -m venv ./.gradle/python")
        }
    }
}

tasks.named("test") {
    dependsOn("createVirtualEnv")
    finalizedBy("performTests")
}

gitSemVer {
    buildMetadataSeparator.set("-")
    maxVersionLength.set(20)
}

tasks.register<ru.vyarus.gradle.plugin.python.task.PythonTask>("qualityCode") {
    command = "-m flake8 --extend-ignore ${flakeExcludeTypes.joinToString(separator = ", ")} src"
}

tasks.register<ru.vyarus.gradle.plugin.python.task.PythonTask>("execSub") {
    command = "src/main/python/applicationServices/sample/servicebus_sub.py"
}

tasks.register<ru.vyarus.gradle.plugin.python.task.PythonTask>("execPub") {
    command = "src/main/python/applicationServices/sample/servicebus_pub.py"
}

tasks.register<ru.vyarus.gradle.plugin.python.task.PythonTask>("setup") {
    command = "setup.py install"
}

tasks.register<ru.vyarus.gradle.plugin.python.task.PythonTask>("cleanSetup") {
    command = "setup.py clean --all install"
}

tasks.register<ru.vyarus.gradle.plugin.python.task.PythonTask>("execMain") {
    workDir = "./src/main/"
    command = "-m IntelligentBackpackService"
}

tasks.register<Delete>("cleanDoc") {
    val directoryPath = "$projectDir/docs"
    val file = File(directoryPath)
    if (file.isDirectory) {
        delete(file)
    }
}

tasks.register<Delete>("deleteMovedDocumentation") {
    val directoryPath = "$projectDir/docs/python"
    val file = File(directoryPath)
    if (file.isDirectory) {
        delete(file)
    }
}

tasks.register<Copy>("moveReports") {
    from(layout.projectDirectory.file("./docs/python"))
    into(layout.projectDirectory.dir("./docs"))
}

tasks.register<ru.vyarus.gradle.plugin.python.task.PythonTask>("generateDocumentation") {
    dependsOn("cleanDoc")
    command = "-m pdoc --html ./src/main/python --output-dir ./docs"
    finalizedBy("moveReports")
    finalizedBy("deleteMovedDocumentation")
}

/*tasks.named("check").configure {
    dependsOn(tasks.named("qualityCode"))
}*/

// copia i file da trasferire in una folder distribution
tasks.register<Copy>("copyDistribution") {
    from(layout.projectDirectory.file("src/"))
    into(layout.buildDirectory.dir("distribution"))
}

tasks.create("deploy") {
    val password: String? by project
    val distributionDir = layout.buildDirectory.dir("distribution").get().asFile
    doLast {
        val sshClient = SshClient.setUpDefaultClient()
        try {
            sshClient.start()
            val session: ClientSession = sshClient.connect("pi", "192.168.1.40", 22)
                .verify(1000)
                .session

            session.addPasswordIdentity(password)
            session.auth().verify(1000)

            val creator = ScpClientCreator.instance()
            val client = creator.createScpClient(session)

            client.upload(
                distributionDir.path,
                "/home/pi/Desktop/intelligentbackpack",
                ScpClient.Option.Recursive,
                ScpClient.Option.PreserveAttributes,
                ScpClient.Option.TargetIsDirectory
            )

            session.executeRemoteCommand("chmod -R u+x /home/pi/Desktop/intelligentbackpack/distribution")

            session.close()
            sshClient.close()
        } catch (ex: Exception) {
            project.logger.error(ex.message)
        } finally {
        }
    }
}

tasks.create("createPackages") {
    var numPackages = 0
    val path = "$projectDir/src/"
    val dirs = Files.walk(Paths.get(path))
        .filter { Files.isDirectory(it) && !Files.isSymbolicLink(it) }.toList()

    for (folder in dirs) {
        val path = "${folder.toAbsolutePath()}/__init__.py"
        if (!Files.exists(Paths.get(path))) {
            File(path).createNewFile()
            numPackages ++
        }
    }

    println("Created $numPackages packages")
}
