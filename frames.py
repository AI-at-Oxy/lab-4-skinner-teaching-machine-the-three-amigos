"""
Skinner Teaching Machine - Frame Definitions
COMP 395: AI and Learning Technologies

This file contains the instructional frames for your teaching machine.

=============================================================================
YOUR TASK:
=============================================================================
1. Choose a topic you want to teach (5-10 frames minimum)
2. Design your frame structure (see options below)
3. Write frames that follow Skinner's principles:
   - Small steps: Each frame teaches ONE small concept
   - Build sequentially: Later frames build on earlier ones
   - High success rate: Design for ~95% correct answers
   - Clear prompts: Unambiguous fill-in-the-blank or short answer

=============================================================================
FRAME STRUCTURE OPTIONS:
=============================================================================

OPTION A - Minimal:
frame = {
    "prompt": "The capital of France is _____.",
    "answer": "paris"
}

OPTION B - With feedback (RECOMMENDED):
frame = {
    "prompt": "The capital of France is _____.",
    "answer": "paris",
    "feedback_correct": "Correct! Paris is the capital of France.",
    "feedback_incorrect": "Not quite. The answer is Paris."
}

OPTION C - Rich (with hints and multiple answers):
frame = {
    "prompt": "What keyword defines a function in Python?",
    "answer": "def",
    "answers": ["def"],  # List for multiple acceptable answers
    "hint": "It's a 3-letter word.",
    "feedback_correct": "Yes! 'def' is used to define functions.",
    "feedback_incorrect": "Not quite. We use 'def' to define functions.",
    "topic": "python-functions"
}

Choose a structure and be CONSISTENT across all your frames!
=============================================================================
"""

# =============================================================================
# EXAMPLE FRAMES: Introduction to Python Variables
# Replace these with your own topic!
# =============================================================================

FRAMES = [
    # Frame 1: Astronomy
    {
        "prompt": "Astronomy is the study of the _____?",
        "answers": ["stars", "universe", "planets", "galaxies", "space", "celestial objects"],
        "hint": "Think outside of Earth.",
        "feedback_correct": "Yes! Astronomy is the study of celestial objects and the universe.",
        "feedback_incorrect": "Not quite. Astronomy is the study of celestial objects and the universe.",
        "topic": "astronomy"
    },  
    
    # Frame 2: Number of planets
    {
        "prompt": "The number of planets in our solar system is ___?",
        "answers": ["8", "eight", "ocho", "viii"],
        "hint": "It's more than 4!",
        "feedback_correct": "Yes! There are 8 planets in our solar system.",
        "feedback_incorrect": "Not quite. There are 8 planets in our solar system.",
        "topic": "planets"
    },

    # Frame 3: The Fourth Planet
    {
        "prompt": "What is the name of the fourth planet from the Sun?",
        "answers": ["mars"],
        "hint": "It's named after the Roman god of war.",
        "feedback_correct": "Correct! Mars is the fourth planet from the Sun.",
        "feedback_incorrect": "Not quite. The fourth planet from the Sun is Mars.",
        "topic": "astronomy-planets"
    },
    
    # Frame 4: Number of Moons
    {
        "prompt": "How many moons does mars have?",
        "answers": ["2", "two", "dos", "ii"],
        "hint": "It's a single digit number.",
        "feedback_correct": "Yes! Mars has two moons: Phobos and Deimos.",
        "feedback_incorrect": "Mars has two moons: Phobos and Deimos.",
        "topic": "moons"
    },
    
    # Frame 5: Planets Without Moons
    {
        "prompt": "Which planets in the Milky Way Galaxy don't have moons?",
        "answers": ["mercury and venus", "mercury & venus", "venus and mercury", "venus & mercury"],  # List for multiple acceptable answers
        "hint": "These are the two innermost planets.",
        "feedback_correct": "Correct! Mercury and Venus are the only planets in the Milky Way Galaxy without moons.",
        "feedback_incorrect": "Not quite. The answer is Mercury and Venus.",
        "topic": "planets-without-moons"
    },
    # Frame 6: Hottest Planet
    {
        "prompt": "Which planet has the hottest surface?",
        "answers": ["venus"],
        "hint": "It's the second planet from the Sun.",
        "feedback_correct": "Correct! Venus has the hottest surface in our solar system.",
        "feedback_incorrect": "Not quite. The answer is Venus.",

        "topic": "Hottest Planet"
    },
   
]


# =============================================================================
# TIPS FOR WRITING GOOD FRAMES:
# =============================================================================
# 
# 1. START EASY: First frames should be very simple
# 
# 2. ONE CONCEPT PER FRAME: Don't combine multiple ideas
# 
# 3. USE BLANKS STRATEGICALLY: 
#    "In Python, we use _____ to define a function."
#    Not: "What do we use to define a function in Python?"
# 
# 4. BUILD ON PREVIOUS FRAMES: Frame 5 can reference concepts from Frame 3
# 
# 5. ANTICIPATE ERRORS: Your feedback_incorrect should address common mistakes
# 
# 6. NORMALIZE ANSWERS: The app converts to lowercase and strips whitespace,
#    but consider if "=" and "equals" should both be accepted
#
# =============================================================================
