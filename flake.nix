
{ 
  description = "Python ML dev env";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  };

  outputs = {self, nixpkgs}: let 
      system = "x86_64-linux"; 
      pkgs = import nixpkgs { inherit system; };

  in {
      devShells.${system}.default = pkgs.mkShell {
       packages = with pkgs; [
      (python312.withPackages (python-pkgs: with python-pkgs; [
        pandas
        # requests
        numpy
        pandas
        scipy
        scikit-learn 
        tensorflow
        # pymc
        dm-tree
        # arviz
        matplotlib
        seaborn
        selenium
        # beautifulsoup4
        # pymongo
        # plotly
        # toolz
      ]))
        ty
        ruff
      ];

        shellHook = ''
          venv="$(cd $(dirname $(which python)); cd ..; pwd)"
          ln -Tsf "$venv" .venv
          echo "Python environment loaded. Virtual env linked to .venv"
          exec zsh
        '';
      };
    };
}
