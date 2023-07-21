# IntelligentBackpack
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=IntelligentBackpack_IntelligentBackpack&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=IntelligentBackpack_IntelligentBackpack)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=IntelligentBackpack_IntelligentBackpack&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=IntelligentBackpack_IntelligentBackpack)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=IntelligentBackpack_IntelligentBackpack&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=IntelligentBackpack_IntelligentBackpack)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=IntelligentBackpack_IntelligentBackpack&metric=bugs)](https://sonarcloud.io/summary/new_code?id=IntelligentBackpack_IntelligentBackpack)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=IntelligentBackpack_IntelligentBackpack&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=IntelligentBackpack_IntelligentBackpack)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=IntelligentBackpack_IntelligentBackpack&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=IntelligentBackpack_IntelligentBackpack)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=IntelligentBackpack_IntelligentBackpack&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=IntelligentBackpack_IntelligentBackpack)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=IntelligentBackpack_IntelligentBackpack&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=IntelligentBackpack_IntelligentBackpack)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=IntelligentBackpack_IntelligentBackpack&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=IntelligentBackpack_IntelligentBackpack)


This repository refers to the Raspberry Pi 4 implementation of the Intelligent Backpack.
First of all connect the RFID module correctly, with the following wire connections:

| Pin RC522   | Pi Header         |
|:------------|:------------------|
| 3.3V        | 1                 |
| RST         | 22                |
| GND         | 6                 |
| IRQ         | //                |
| MISO        | 21                |
| MOSI        | 19                |
| SCK         | 23                |
| NSS or SDA  | 24                |

Be sure to have installed the mfrc522 python library in your Raspberry.
Then, run the following Gradle command to execute the project after the building process:
```bash
./gradlew execMain
```