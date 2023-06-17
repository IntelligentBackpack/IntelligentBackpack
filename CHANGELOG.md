## [1.0.3](https://github.com/IntelligentBackpack/IntelligentBackpack/compare/1.0.2...1.0.3) (2023-06-17)


### Bug Fixes

* changed imports ([9dfe619](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/9dfe6197f1f5b5fa43aefe784687049c986e0f56))


### General maintenance

* code quality improved and removed unused scripts ([0774c48](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/0774c48319d5a6f92ab6184dddbd900c86d0ef21))


### Documentation

* added new documentation ([17faa3f](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/17faa3f5609ba299ad88ce7bbfdc5962d4f0aade))
* updated documentation for GitHub Pages ([79909bd](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/79909bd02096cb599f95b0ea78f2409470cc898d))

## [1.0.2](https://github.com/IntelligentBackpack/IntelligentBackpack/compare/1.0.1...1.0.2) (2023-06-16)


### Bug Fixes

* fixed write_username arguments ([f667fd6](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/f667fd6c3a0450f58182bc27d26ba11d2be8d28b))


### General maintenance

* added path to write_username ([115960a](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/115960a18b7d1eaea8dccd1fecb72984c378094c))
* changed local registration of the user ([b968628](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/b968628d75c28e8ac2abf31d3c36364227a47f78))


### Build and continuous integration

* changed python execution scope ([2da9c25](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/2da9c2568de28e81a662e4de470c4779c03cd385))

## [1.0.1](https://github.com/IntelligentBackpack/IntelligentBackpack/compare/1.0.0...1.0.1) (2023-06-16)


### Bug Fixes

* added startup registration of the username ([650d6ba](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/650d6ba60c2e4efae110dd95e21a6e89bc828eb0))


### General maintenance

* merge resolution ([b278460](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/b27846089830effee502a6234df123ef1225b083))

## 1.0.0 (2023-06-16)


### Features

* adapted RestModule with a Thread and restFul utils methods ([23c683f](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/23c683fc760928bd97d044a9e17cdbb09da1c740))
* adapted RFID module with a thread ([5c00f3b](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/5c00f3b487abcb2709bf5844ea5647f875a011d7))
* added new backpack entity, to store backpack state ([1386661](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/1386661f9f2123bd51fdf19720a8b63a33a342e6))
* added new basic tools ([641980a](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/641980ac24955e6e42a047218b7f9ccee47a1d59))
* added new getAllTags to LocalRepository and minor things fixed ([f14a73c](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/f14a73c8eef7b9cc78028e0b7f3a2c80eb1f331e))
* added new method for PUT requests ([40015e5](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/40015e5c3204f118f4c1a600ee66b09b6470d197))
* added new method to save and retrieve username from disk ([0bcfd31](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/0bcfd312a013d4d1f1b5220ed7d4790b3c23505e))
* added new preferences application utils ([1c936b7](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/1c936b78ac041a4c4e1ac674086e9d029db9cf82))
* added new RemoteRepository class to manage Realtime Firebase db ([4ee0095](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/4ee0095ae1244e3123d2225f28680fc14a52c19b))
* added new repository architecture and first test example to be implemented ([7452c0d](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/7452c0d5fe8bb250ed1abb6baabf480b2d4d24b1))
* added new RFID and Led modules ([89a75ad](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/89a75adbeb2dd393e0079bc17e2d70204645aa38))
* added new startup sync between local and remote db ([f3b0803](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/f3b08035f5a76cec5ca1b379bfa5b6e71012dbc3))
* added repository factory ([12aa6cc](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/12aa6ccdd0f9a9275279f343f64accdceca5eebc))
* added sample python classes and src packages ([28edb30](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/28edb30adeb946d17a8a10aad8c55f72d5e9b1dd))
* removed old files and added new RFID and HubIot modules ([25c88c5](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/25c88c59c19cf0cfad1b4bb5b709509b82c0f3c0))
* **test:** added new entities and value objects tests ([b84c62b](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/b84c62b25415c9ba7504be3b463d9f6241e327f4))
* **test:** added new tests for local database ([660a96e](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/660a96e3e25f03fd4f279b364732583f1d3c2ac0))


### Bug Fixes

* adapted the whole repository architecture to work with sync queue ([0d5cc30](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/0d5cc3028dc330b96200a56193e34ba660678ca3))
* added new preferences values reader and fixed hut iot connection string construction ([0fe599c](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/0fe599c4bf8f5d9262928b1f52cea9cae46ba623))
* **build:** fixed command as list ([02faf25](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/02faf25fae68bc41d52149d890ecb520302a77d3))
* **build:** fixed command with python3 instead of python ([bb671cd](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/bb671cdc86d8882d4fb1dde47ca5bf3a58bedb5a))
* fixed config file creation with username ([4406d72](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/4406d72f3cc223d006ae94b963e919fc08f8eb75))
* fixed insertion policy array length check ([eb82b6e](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/eb82b6ec7a79993a8bdcf27183adf17079e53f79))
* fixed library imports and added payload ([9c34acd](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/9c34acde0a9475ef2e0eb93c8c344a10b2b46200))
* fixed message processing ([57e3656](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/57e365660a26bd96577624a41901b756159d552d))
* fixed messages queue name and minor things ([7848663](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/784866321bb0f06853a818dcf8a8154e0ab531a2))
* fixed policy check value ([0dae41f](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/0dae41f863a1ca8710d566b3fca806ee652ee553))
* fixed remote repo value to write and set username ([a67086b](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/a67086b4ca51538a2eac4c6b5e3e9fcf225dc77c))
* fixed rfid preprocess with padding values ([18635ca](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/18635cae9e7a5edb010599cf4f30b4f2dbccbe2f))
* fixed rfid tag processing with hex parsing ([5f79a26](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/5f79a26772658ca467d78eecf297ad0651757333))
* fixed user creation and backpack service that set the backpack id ([78fae45](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/78fae45cbb4edb1860e4f678b4074060c6b1993a))
* fixed user email formatting in rest calls ([769b20b](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/769b20b4652d5974297a19b150b39f5c06b36c27))
* fixed user email getter into testBackpack ([faa289f](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/faa289f9c9a6b5f12de21f55e998806b7f098a92))
* fixed user validation and hash usage into repository ([1ca409e](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/1ca409efded3c287c9298e75d06cdf086e7bcfb7))
* removed condition variable and adapted to use sync queue ([e136552](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/e136552cf9b89a7c27ad2249e0221ddd0a91353e))


### Documentation

* added documentation for unregister ([d36d5e7](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/d36d5e754d583ed16af66659d5334308d3ecaf42))
* added new generated documentation files for github pages ([f89969f](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/f89969fd68615a1de7aed07b7e7de1c85d68970d))


### General maintenance

* added build files ([37db70d](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/37db70de9e0dcec077f1c9c12471d47bf076fd59))
* added comments to Hub Iot module ([353a3b6](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/353a3b63809905d2b76db43db8d9eb3814afa2ef))
* added comments to service locator ([af02cff](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/af02cff1f2362f70263d691da9175c6f47f21800))
* added device config file for demo test purpose ([1bf0492](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/1bf0492eac3f97ecd27bba4d80e2176d7e3b0b8e))
* added docstrings for documentation generation ([c8f6ce9](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/c8f6ce9156345b1e54a81686bca39e4ab610fef2))
* added entities, value objects and domain services ([7bdab9f](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/7bdab9fe8fa7ffd1429204df7dc07829cdbd3917))
* added ktlint config file ([e9431f6](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/e9431f68f20edfcba30ae78f53e4a98cfb8d8a15))
* added network and rfid threads execution ([599e9af](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/599e9af74e9446b96815abb4597c8df12288c11f))
* added new docs generation tasks ([bd5292a](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/bd5292a6f9181ba0ff255620478fec625aa12159))
* added new module into service locator ([8c5839c](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/8c5839c9609958ccba8b1eaadb7e1c77f4daa3ea))
* added new packages to separate different modules ([ca7bffa](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/ca7bffabad103b75ae574864aeda9234e09683ff))
* added new service locator usage into the program entry point ([a81a9e6](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/a81a9e6024a127402415db04f1c8411e22cd458f))
* added policies and empty entities to be implemented ([a55128e](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/a55128e006fad745d031f706738004ae256bacde))
* added rfid preprocessing ([6fca740](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/6fca740da13aad4aae445c06cdb60b2cdee85833))
* added service locator and sync utils for concurrency ([a82a518](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/a82a51893c6f279abe000ed1d38b58a4150a5ac5))
* added username to config file for demo purpose ([9b7f54b](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/9b7f54bb808c6cde469dc9a721bf00bb06e17fd4))
* created basic tools scripts ([a7674d9](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/a7674d9effa4be6738869636d364d5c2e519b225))
* fixed BackpackLogic service to find elements and correctly use the insertion policy ([37b8a88](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/37b8a888600ffc285000b58513e17e77a8e4df08))
* fixed setup packages file ([eacafe2](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/eacafe298e240020739632af733ee094527fb8d7))
* fixed setup.py file ([4ae7fd1](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/4ae7fd195ffaf00cb4cb65bcc91224823d89b54b))
* fixed sintax ([9122d31](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/9122d3135cab21983f307c90c0a9c4a5ce58e24a))
* modified backpack and book objects and minor things fixed ([8c6f092](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/8c6f092968ac8cecf937b1456128943a47e34821))
* moved sample folder ([c5d7704](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/c5d77048f1d2b1c8611497ddfadb6600c83c23f8))
* moved test files and changed imports syntax ([219409d](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/219409dc2745d17ac317ee901a7fb164c9b9bb24))
* removed empty init files to clean repo structure ([734aa67](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/734aa676f3807d1162f6b371fc09ffe4dbdf63e7))
* removed useless classes ([7236677](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/7236677106da12c84b0fb2ee163653f87b5b3864))
* updated a dependency version ([c973b58](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/c973b589314faf2cf49b199c8fa93c1a183c519e))
* updated gitignore ([bc0cb0b](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/bc0cb0b704f5a5c351175df965b5ed34b069b3bf))


### Build and continuous integration

* added .gradle and .idea folder to gitignore ([164ebae](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/164ebaef1fae52dc314c148125c4604d08b8f0c3))
* added build folder to gitignore ([d0cb5f2](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/d0cb5f2a75172f49a90c1576e880ffee3775428c))
* added build step within test job ([85e4a0c](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/85e4a0c61310a42da2ef2172a4a6eed255141ae2))
* added documentation generation tasks ([61d3b00](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/61d3b006c5c65ddb02e8449f66e5a27b4a76dd20))
* added new buildscript and python dependencies ([b5b791e](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/b5b791e385124ee16a120381cf169544fc69b939))
* added new pre commit checks and qa checks ([dfb789f](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/dfb789f46d05c2a2d09ba31795224885689dd81c))
* added new pytest plugin, dependencies and project management tasks ([6f0d6fb](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/6f0d6fb7c3a2376b5d7fd472f11697d1e838bf75))
* added new remote deploy task for remote devices ([edb6e5f](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/edb6e5f1f810b87efbef4d3b0c857bd386021dea))
* added pipeline ([7f81c67](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/7f81c67ba5d9bbcfa43e71cb89928cd253f199d8))
* added push branch configuration ([cd4de71](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/cd4de71f9218616396c3fb0cc75ddc15b4ee4c15))
* added python test plugin dependency over the test task ([4147d92](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/4147d92a52e74e68b45e52164d8a59b3779b2ee6))
* added task to create virtual environment ([6c1d92b](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/6c1d92b47d513f6864e10d70dbbae6a63a0c6897))
* added test task dependency ([d341261](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/d341261ba4c61de300c9607491eba06e271ce247))
* changed flake version and python context execution ([22e568e](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/22e568e8c526ab4b8e79ff2424d4974dd513d465))
* fixed ci pipeline with new job ([26a42f3](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/26a42f3a3383261802a4dbdec20a3410326d938b))
* fixed ci pipeline with new step ([64f5f7f](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/64f5f7f649fb83b5e049d99694744a29610e5aad))
* fixed ci testing environment ([9892486](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/9892486a7a221b9a75d1e2f92f813044770f10c0))
* fixed command text formatting ([f990933](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/f9909335c872d68070a4ff858e214c92a1082b23))
* fixed documentation generation tasks regarding the correct location ([d186b39](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/d186b3920c5909caf8a7b7021ff46213459c2a43))
* new servicebus dependency, set test plugin, run tasks and updated .gitignore ([1cd8599](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/1cd8599dc3a6d11cf28053fb8c887c2d80d7edbe))
* reduced min coverage percent value ([33e194d](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/33e194da26817f209971f2d089f71bb03ae97bfe))
* removed service-bus dependency and minor task names changed ([7320daf](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/7320daffbf703ac4da1264298f449d6ef9e90417))
* updated ci with new release job ([32bf7d6](https://github.com/IntelligentBackpack/IntelligentBackpack/commit/32bf7d63c3a7af15b5204d480c6d0b7581109ae1))
