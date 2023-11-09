# pythoneda-sandbox/python-artifact-infrastructure

Infrastructure layer for <https://github.com/pythoneda-sandbox/python-artifact>.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-sandbox/python-artifact-infrastructure-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-sandbox-python-artifact-infrastructure = {
      [optional follows]
      url =
        "github:pythoneda-sandbox/python-artifact-infrastructure-artifact/[version]?dir=python-artifact-infrastructure";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-sandbox/python-artifact-infrastructure-artifact/tree/main/python-artifact-infrastructure](python-artifact-infrastructure "python-artifact-infrastructure") folder of <https://github.com/pythoneda-sandbox/python-artifact-infrastructure-artifact>.


