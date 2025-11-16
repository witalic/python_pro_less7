# CLAUDE.md - AI Assistant Guide for python_pro_less7

## Project Overview

This is a **Python learning project** (Lesson 7) that implements a simple console-based note-taking application using the Model-View-Presenter (MVP) architectural pattern. The project serves as an educational example demonstrating:

- MVC/MVP architecture patterns in Python
- CRUD operations (Create, Read, Update, Delete, List)
- Exception handling and decorators
- Regular expressions
- Python coding conventions

## Codebase Structure

```
python_pro_less7/
├── models.py       # Data layer - stores notes in memory
├── presenter.py    # Presentation/Controller layer - business logic
├── views.py        # View layer - user interface and main loop
├── learn.py        # Learning/practice file with examples
└── README.md       # Project documentation (currently minimal)
```

## File Descriptions

### models.py
- **Purpose**: Data model layer
- **Contents**: Defines the global `notes` list that stores all notes in memory
- **Encoding**: cp1251 (Cyrillic/Russian)
- **Key Elements**:
  - `notes = []` - In-memory storage for all notes

### presenter.py
- **Purpose**: Presenter/Controller layer containing business logic
- **Encoding**: cp1251 (Cyrillic/Russian)
- **Key Functions**:
  - `create_note()` - Creates a new note with title and text (Russian prompts)
  - `list_elements(elements)` - Displays enumerated list of elements
  - `get_note(notes)` - Retrieves a note by user-selected number
  - `limit_page()` - Prints separator line for UI formatting
- **Dependencies**: Imports `notes` from models.py
- **Data Structure**: Notes are dictionaries with `'title'` and `'text'` keys

### views.py
- **Purpose**: View layer - main application loop and user interface
- **Encoding**: cp1251 (Cyrillic/Russian)
- **Functionality**: Console menu with 6 options:
  1. Create - Add new note
  2. List - Show all notes
  3. Read - Display specific note
  4. Update - Modify existing note
  5. Delete - Remove note
  6. Exit - Quit application
- **Dependencies**: Imports all from presenter.py (which imports notes from models.py)
- **Flow**: Infinite loop until user selects exit option

### learn.py
- **Purpose**: Educational examples and practice code
- **Encoding**: cp1251 (Cyrillic/Russian)
- **Contents** (mostly commented out):
  - Nested functions example
  - Exception handling (try/except)
  - Custom exception raising with type validation
  - Decorator pattern (try_decorator)
  - Regular expressions with `re` module
  - Pattern matching examples (phone numbers, user filtering)
- **Note**: All code is commented out - this is a reference/learning file

## Architecture Pattern

The project follows the **Model-View-Presenter (MVP)** pattern:

```
┌──────────┐     imports     ┌─────────────┐     imports     ┌─────────┐
│ views.py │ ─────────────> │ presenter.py│ ─────────────> │models.py│
│  (View)  │                │ (Presenter) │                │ (Model) │
└──────────┘                └─────────────┘                └─────────┘
    │                              │                             │
    │ User Interaction         Business Logic              Data Storage
    │ Console I/O              CRUD Functions              In-memory list
```

**Data Flow**:
1. User interacts with console menu (views.py)
2. View calls presenter functions (presenter.py)
3. Presenter manipulates data model (models.py)
4. Results flow back through presenter to view

## Development Conventions

### Encoding
- **Character Encoding**: cp1251 (Windows Cyrillic)
- **All files** start with `# -*- coding: cp1251 -*-`
- **UI Text**: Russian language prompts and messages
- **Important**: When editing files, maintain cp1251 encoding for Cyrillic text

### Code Style
- No type hints used
- Simple, procedural style
- Dictionary-based data structures
- Global state (notes list)
- No external dependencies (stdlib only)

### Naming Conventions
- **Functions**: snake_case (e.g., `create_note`, `list_elements`)
- **Variables**: snake_case (e.g., `notes`, `number`, `choice`)
- **Constants**: None defined in this project

## Data Model

### Note Structure
```python
note = {
    'title': str,  # Note title/heading
    'text': str    # Note content/body
}
```

### Storage
- **Type**: In-memory Python list
- **Persistence**: None - data lost on program exit
- **Location**: `models.notes` global variable
- **Operations**: Direct list manipulation (append, remove, update)

## Common Development Tasks

### Adding a New Field to Notes

1. **Update `create_note()` in presenter.py**:
   ```python
   note = {
       'title': input('Title: '),
       'text': input('Text: '),
       'new_field': input('New Field: ')  # Add this
   }
   ```

2. **Update display logic** in `list_elements()` if needed

### Adding Persistence (File Storage)

1. Create save/load functions in models.py
2. Import `json` module
3. Add save call after modifications in views.py
4. Load notes on startup in views.py

### Adding Input Validation

1. Create validation functions in presenter.py
2. Use try/except blocks for error handling
3. Return None or raise exceptions for invalid input
4. Update views.py to handle validation errors

### Internationalization

1. Extract all Russian strings to a dictionary
2. Create language files or use gettext
3. Replace hardcoded strings with translations
4. Update encoding if using Unicode languages

## Key Implementation Details

### Note Selection Pattern
```python
# Used in views.py for read, update, delete
note = get_note(notes)  # Shows list, gets user selection
# Then operate on the selected note
```

### Update Pattern
```python
# views.py line 20-21
note = get_note(notes)
note.update(create_note())  # Dict.update() merges dictionaries
```

### Error Handling
- **Current**: Minimal error handling
- **Input validation**: `number.isdigit()` check in `get_note()` (presenter.py:18)
- **Index bounds**: `0 < int(number) <= len(notes)` check
- **Improvement opportunities**: Add try/except for invalid inputs, empty lists

## Development Workflow

### For New Features

1. **Plan the change**: Identify which layer(s) need modification
2. **Start with models.py**: If data structure changes
3. **Update presenter.py**: For new business logic
4. **Modify views.py**: For UI changes
5. **Test manually**: Run the application and test all paths

### For Bug Fixes

1. **Identify the layer**: Model, Presenter, or View
2. **Read the relevant file**: Understand current implementation
3. **Make targeted fix**: Modify only what's necessary
4. **Test edge cases**: Empty lists, invalid inputs, boundaries

### For Code Improvements

1. **Maintain architecture**: Keep separation of concerns
2. **Preserve encoding**: Keep cp1251 for Russian text
3. **Add validation**: Improve error handling gradually
4. **Consider persistence**: File I/O for permanent storage

## Git Workflow

### Branch Strategy
- **Current branch**: `claude/claude-md-mi1hk0fz6z3bxg7e-0175tAh19MunKya7G4ivnG6P`
- **All development** should be on this feature branch
- **Commit conventions**: Short, descriptive messages (see git log)

### Commit Examples (from history)
```
801c182 cont. learn
f8fc455 add presenter
d7fff6e test
758c5d9 add readme
```

### Push Requirements
- Always use: `git push -u origin <branch-name>`
- Branch must start with `claude/` and match session ID
- Retry network failures with exponential backoff (2s, 4s, 8s, 16s)

## Important Notes for AI Assistants

### When Editing Files

1. **Always read first**: Use Read tool before any Edit/Write operations
2. **Preserve encoding**: Maintain `# -*- coding: cp1251 -*-` header
3. **Keep Russian text**: Don't translate UI strings unless asked
4. **Maintain architecture**: Respect the MVP layer separation
5. **Test implications**: Consider how changes affect all layers

### When Adding Features

1. **Follow MVP pattern**: Put logic in the right layer
2. **Update all layers**: If data model changes, update presenter and view
3. **Maintain consistency**: Use existing patterns (e.g., `get_note()` pattern)
4. **Consider errors**: Add validation and error handling
5. **Document changes**: Update this CLAUDE.md if architecture changes

### When Debugging

1. **Check data flow**: Model → Presenter → View
2. **Verify imports**: Circular import prevention (views imports presenter imports models)
3. **Test boundaries**: Empty lists, invalid indices, bad input
4. **Check encoding**: Cyrillic text issues may be encoding-related

### Known Limitations

1. **No persistence**: Notes lost when program exits
2. **No search**: Only sequential list display
3. **No categories**: Flat note structure
4. **No timestamps**: Creation/modification dates not tracked
5. **No multi-user**: Single-session, in-memory storage
6. **Minimal validation**: Basic input checking only
7. **No tests**: No unit tests or test framework

### Improvement Opportunities

- Add JSON file persistence
- Implement search/filter functionality
- Add timestamps and metadata
- Create proper exception handling
- Add input validation and sanitization
- Implement categories/tags
- Add unit tests
- Create configuration file for settings
- Add logging for debugging
- Internationalization support

## Quick Reference

### Running the Application
```bash
python views.py  # Start the note-taking application
```

### Testing Examples in learn.py
```bash
python learn.py  # Currently does nothing (all code commented)
# Uncomment sections to test decorators, regex, etc.
```

### File Dependencies Graph
```
views.py → presenter.py → models.py
learn.py (standalone, no dependencies)
```

### Key Functions Reference

| Function | File | Purpose |
|----------|------|---------|
| `create_note()` | presenter.py:4 | Create new note dictionary from user input |
| `list_elements()` | presenter.py:11 | Display enumerated list of items |
| `get_note()` | presenter.py:15 | Get note by user-selected number |
| `limit_page()` | presenter.py:22 | Print separator line |

## Version Information

- **Python Version**: Python 3.x (no version constraints specified)
- **Dependencies**: None (stdlib only)
- **Encoding**: cp1251 (Windows Cyrillic)
- **Last Updated**: 2025-11-16

## Contact & Context

This is a learning project (Lesson 7) focused on demonstrating Python concepts and architectural patterns. The codebase is intentionally simple for educational purposes.

---

**Last Generated**: 2025-11-16 by Claude AI Assistant
**Repository**: /home/user/python_pro_less7
**Branch**: claude/claude-md-mi1hk0fz6z3bxg7e-0175tAh19MunKya7G4ivnG6P
