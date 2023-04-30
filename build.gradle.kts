plugins {
    kotlin("jvm") version "1.5.31"
    id("ru.vyarus.use-python") version "3.0.0"
    alias(libs.plugins.gitSemVer)
}

group = "org.SmartBag"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

gitSemVer {
    buildMetadataSeparator.set("-")
    maxVersionLength.set(20)
}
