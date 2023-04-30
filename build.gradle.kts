plugins {
    kotlin("jvm") version "1.5.31"
    id("ru.vyarus.use-python") version "3.0.0"
    alias(libs.plugins.gitSemVer)
    alias(libs.plugins.kotlin.qa)
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
