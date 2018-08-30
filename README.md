# conan-tacopie

[Conan.io](https://conan.io) package for [TacoPie library](https://github.com/Cylix/tacopie)

| Appveyor | Travis |
|-----------|--------|
|[![Build Status](https://ci.appveyor.com/api/projects/status/github/db4/conan-tacopie?branch=master&svg=true)](https://ci.appveyor.com/project/db4/conan-tacopie)|[![Build Status](https://travis-ci.org/db4/conan-tacopie.svg?branch=master)](https://travis-ci.org/db4/conan-tacopie)|

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload conan-tacopie/3.2.0@dbely/stable --all

## Reuse the packages

### Basic setup

    $ conan install conan-tacopie/3.2.0@dbely/stable

### Project setup

If you handle multiple dependencies in your project, it would be better to add a *conanfile.txt*

    [requires]
    conan-tacopie/3.2.0@dbely/stable

    [generators]
    txt
    cmake


