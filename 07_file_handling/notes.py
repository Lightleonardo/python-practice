def add_note(filename, text):
    """Appends one line to a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def read_notes(filename):
    """Reads the lines from a text file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

# Demonstration of both functions
if __name__ == "__main__":
    notes_filename = "notes.txt"

    # Add two notes
    add_note(notes_filename, "First note.")
    add_note(notes_filename, "Second note.")

    # Read all notes and print with line numbers
    notes = read_notes(notes_filename)
    for line_number, note in enumerate(notes, start=1):
        print(f"Note {line_number}: {note}")