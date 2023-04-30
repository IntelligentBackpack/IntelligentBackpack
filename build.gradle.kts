import java.nio.file.Files
import java.nio.file.Paths

plugins {
    kotlin("jvm") version "1.5.31"
    id("ru.vyarus.use-python") version "3.0.0"
    alias(libs.plugins.gitSemVer)
    alias(libs.plugins.kotlin.qa)
}

group = "org.IntelligentBackpack"

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

python {
    pip("pycco:0.6.0")
    pip("coverage:7.2.2")
    pip("flake8:6.0.0")
    pip("gpiozero:1.6.2")
    pip("mfrc522:0.0.7")
    minPythonVersion = "3.2"
    minPipVersion = "9.0.1"
    python.scope = ru.vyarus.gradle.plugin.python.PythonExtension.Scope.VIRTUALENV
}

gitSemVer {
    buildMetadataSeparator.set("-")
    maxVersionLength.set(20)
}

tasks.register<ru.vyarus.gradle.plugin.python.task.PythonTask>("qualityCode") {
    command = "-m flake8 src"
}

tasks.register<Delete>("cleanDoc") {
    delete(fileTree("./").matching {
        include("*.html")
    })
}

tasks.register<Copy>("moveReports") {
    from("./")
    include("*.html")
    into(layout.buildDirectory.dir("doc"))
    finalizedBy("cleanDoc")
}

tasks.register<ru.vyarus.gradle.plugin.python.task.PythonTask>("generateDocumentation") {
    if(!Files.exists(Paths.get("./doc")))
        File("./doc").mkdir()
    command = "-m pydoc -w .\\"
    finalizedBy("moveReports")
}

tasks.named("check").configure {
    dependsOn(tasks.named("qualityCode"))
}
