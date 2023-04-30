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
