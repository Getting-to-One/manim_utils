{ pkgs ? import <nixpkgs> { } }:
with pkgs.python3Packages;

pkgs.mkShell {
  packages = with pkgs; [
    python3
    manim
  ];
}
