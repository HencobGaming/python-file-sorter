from pathlib import Path
import shutil


def sort_files_by_type(base_path: Path) -> None:
    if not base_path.exists() or not base_path.is_dir():
        print("The provided location does not exist or is not a folder.")
        return

    # Destination root for sorted files.
    sorted_root = base_path / "sorted_files"
    sorted_root.mkdir(exist_ok=True)

    moved_count = 0

    for item in base_path.iterdir():
        if not item.is_file():
            continue
        if item.parent == sorted_root:
            continue

        extension = item.suffix.lower().lstrip(".")
        folder_name = extension if extension else "no_extension"
        destination_folder = sorted_root / folder_name
        destination_folder.mkdir(exist_ok=True)

        destination_file = destination_folder / item.name
        duplicate_index = 1
        while destination_file.exists():
            destination_file = destination_folder / f"{item.stem}_{duplicate_index}{item.suffix}"
            duplicate_index += 1

        shutil.move(str(item), str(destination_file))
        moved_count += 1

    print(f"Done. Moved {moved_count} file(s) into: {sorted_root}")


def main() -> None:
    location_input = input("Enter the folder location to sort files: ").strip().strip('"')
    target_path = Path(location_input)
    sort_files_by_type(target_path)


if __name__ == "__main__":
    main()
