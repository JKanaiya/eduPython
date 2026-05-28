
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
      (python313.withPackages (python-pkgs: with python-pkgs; [
        # requests
        numpy
        pandas
        torch
        scipy
        scikit-learn 
        sentencepiece
        sacrebleu
        rouge-score
        seqeval
        sklearn-compat
        nltk
        spacy
        transformers
        spacy-transformers
        hf-xet
        rich
        notebook
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
          pip install sklearn-crfsuite
          echo "Python environment loaded. Virtual env linked to .venv"
          exec zsh
        '';
      };
    };
}
