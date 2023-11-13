{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.fontforge
    pkgs.python3Packages.fontforge
  ];

  shellHook = ''
    echo "Environment prepared. You can now run your FontForge scripts."
  '';
}
