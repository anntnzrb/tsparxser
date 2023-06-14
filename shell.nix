{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python310Packages.pip
    pkgs.poetry

    # misc
    pkgs.python310Packages.flake8
  ];
}
