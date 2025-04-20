import argparse

from module_creator import ModuleCreator



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unreal module creator")
    parser.add_argument("--config", type=str, help="Config file")
    args = parser.parse_args()

    if args.config:
        module_window = ModuleCreator(config_path=args.config)
        module_window.show()
    else:
        print(parser.format_help())
        input("Press Enter to continue...")
        exit()

    

    










