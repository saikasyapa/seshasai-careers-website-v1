{ pkgs }: {
  deps = [
    pkgs.mysql
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server  
  ];
}