import os

def remove_zone_files(folder):
    removed = []
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(":Zone.Identifier"):
                full_path = os.path.join(root, f)
                try:
                    os.remove(full_path)
                    removed.append(full_path)
                except Exception as e:
                    print(f"❌ Error deleting {full_path}: {e}")
    return removed

if __name__ == "__main__":
    import sys
    folder = sys.argv[1] if len(sys.argv) == 2 else "."
    removed = remove_zone_files(folder)
    
    print(f"\n✅ Removed {len(removed)} Zone.Identifier files:")
    for path in removed:
        print(f" - {path}")