# 📚 Grade Guardian

*The student tracker that actually validates your data before everything explodes.*

## What's This About?

So here's the thing: I was learning Pydantic (basically Python's way of saying "hey, let's make sure your data isn't garbage"), and I needed a real project to practice on. Teachers deal with student grades all the time, and honestly, a lot of grade tracking is still done in Excel or even *on paper* (wild, I know).

This is a CLI tool that:
- Takes student data (name, grades, email, etc.)
- Validates EVERYTHING (no more "age: banana" crashing your program at 3 am)
- Calculates averages, assigns letter grades, tracks who's passing/failing
- Saves it all to JSON so you don't lose everything
- Generates nice reports because data is only useful if you can actually read it

Is it over-engineered for what it does? Maybe. But I learned a ton building it, and that's the point.

## Why I Built This

I'm working through a Pydantic crash course and wanted to build something that:
1. Actually validates complex data (not just "hello world" examples)
2. Could theoretically be useful in the real world
3. Shows I understand data modelling, validation, and error handling
4. Doesn't bore me to tears while building it

Plus, this is part of my broader goal of building a personal AI agent that can handle messy real-world data. Baby steps.

## Features That Actually Work

✅ **Smart Validation**
- Ages must be 16-25 (college students)
- Grades between 0-100 (no 150% extra credit nonsense)
- Valid email format (basic but catches typos)
- Alphanumeric student IDs only

✅ **Automatic Calculations**
- Grade averages (with actual rounding, not 87.3333333333)
- Letter grades (A-F, the classics)
- Pass/fail status (60+ is passing)

✅ **Classroom Analytics**
- Class average
- Top performers
- Students who need help (< 60%)
- Full performance reports

✅ **Data Persistence**
- Save to JSON
- Load previous sessions
- No database required (keeping it simple)

✅ **Error Handling That Doesn't Suck**
- Clear error messages (no cryptic Python tracebacks)
- Graceful failures (bad input won't crash the whole thing)
- Validation happens BEFORE data gets saved

## Getting Started

### Install
```bash
pip install pydantic pydantic-settings
```

That's it. One dependency. I'm not trying to install half of PyPI here.

### Run It
```bash
python main.py
```

Follow the prompts. It's pretty straightforward.

### Quick Demo

Want to see it without typing a bunch of data?
```bash
python demo.py
```

This creates 3 sample students and shows you what the reports look like.

## Example Usage
```
🎓 STUDENT PERFORMANCE TRACKER
============================================================

MENU:
1. Add Student
2. View All Students
3. Generate Report
4. Add Grade to Student
5. Save & Exit
------------------------------------------------------------

Choice: 1

📝 ADD NEW STUDENT
--------------------------------------------------
Name: Bob Marley
Age (16-25): 18
Student ID: CS2025
Email: bob@uni.edu
Course: Computer Science
Grades (comma-separated): 85,90,88,92

✅ Student created successfully!

📊 Bob Marley's Stats:
   Average: 88.75%
   Letter Grade: B
   Status: Passing
```

## Project Structure
```
grade-guardian/
│
├── models.py          # Pydantic models (the magic happens here)
├── main.py            # CLI interface
├── demo.py            # Quick demo with sample data
├── data/              # JSON storage
│   └── students.json
├── output/            # Reports go here
│   └── .gitkeep
├── requirements.txt
└── README.md          # You are here
```

## What I Learned

**Pydantic is powerful:**
- Field validation is built-in (min/max, patterns, custom logic)
- Computed properties are clean (`@computed_field`)
- Error messages are actually helpful
- JSON serialisation is one line of code

**Data validation matters:**
- Catching bad data early saves hours of debugging
- Clear validation rules = fewer support questions
- Type hints + Pydantic = your IDE becomes psychic

**Real-world complexity:**
- Building CRUD operations properly takes thought
- User input is always messier than you expect
- Good error handling is the difference between "usable" and "unusable"

## What's Next?

Some ideas I might add (or you can fork and add):

- [ ] **FastAPI backend** - Turn this into a REST API
- [ ] **PDF reports** - Export performance reports as PDFs
- [ ] **Attendance tracking** - Because why not
- [ ] **Grade weighting** - Exams worth more than homework, etc.
- [ ] **Export to Excel** - Pandas integration for spreadsheet exports
- [ ] **Historical data** - Track performance over multiple semesters
- [ ] **Email notifications** - Auto-email struggling students (with their permission obvs)
- [ ] **Multi-class support** - Manage multiple courses at once

If you want to add any of these, PRs are welcome! I'm still learning, so I'd love to see how others approach problems.

## Known Issues

- **No authentication** - This is a learning project, not production software
- **Single classroom** - Can only track one class at a time (for now)
- **No undo** - Delete a student? Hope you saved recently
- **Terminal only** - No fancy GUI (terminal apps are underrated though)

## Contributing

I'm a student learning Python, so if you see something that could be better, I'd genuinely love to hear about it. Open an issue or PR, and let's learn together.

Things I'd especially appreciate feedback on:
- Better Pydantic patterns
- Cleaner code organisation
- More robust error handling
- Performance improvements (if it ever matters at this scale lol)

## Related Projects

Check out my other learning projects:
- [youtube-quote-hunter](https://github.com/yourusername/youtube-quote-hunter) - Search YouTube transcripts with timestamps
- [pdf-study-buddy](https://github.com/yourusername/pdf-study-buddy) - AI-powered PDF study guide generator

All part of my journey to build a personal AI agent. We're getting there, one project at a time.

## License

MIT - Do whatever you want with this. If it helps you learn Pydantic or manage grades, that's awesome. If you use it in production without adding authentication first... that's on you, buddy.

## Acknowledgments

- **Pydantic docs** - Seriously, some of the best documentation I've read
- **FastAPI** - For making me realise I need to learn Pydantic in the first place
- **Every teacher** - Who inspired this by dealing with manual grade tracking
- **Coffee** - For existing

---

**Made by an Engineering student who's tired of seeing "TypeError: 'NoneType' object is not subscriptable" at 2 am.**

*If this helped you learn something or saved you time, that's all the thanks I need. ⭐ it if you want, or don't—I'm not your supervisor.*

**Current bug count: Unknown (ignorance is bliss)** 😂
