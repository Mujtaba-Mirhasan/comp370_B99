Motivation:
    The goal of this typology is to create a simple, consistent way to label the lines spoken by three Brooklyn Nine-Nine side characters: Charles, Rosa, and Terry. Since sitcom dialogue is usually short, fast, and depends heavily on context, we need a clear category system to make sure the annotations stay reliable across different scenes and episodes.
    To build these categories, I open-coded 100 lines for each character (300 total). From that process, I picked a set of categories that actually fit how these characters talk, while still being specific enough to capture the different themes that show up in their dialogue.





Final Categories:


    Category 1: Police Work

        Definition:
            Lines involving investigations, cases, procedural actions, crime-scene details, interrogations, arrests, evidence, tactics, or professional evaluations tied directly to law enforcement.

        Examples (in):
            - “Peralta… Where are we on the Lincoln Place murder?” — Terry
            - “We got eyes on the bandit. He’s a block away.” — Rosa
            - “All right, let’s get started. Scully, where are you on digitizing the old case files?” — Terry
            - “The puncture wounds aren’t from a knife — I think it’s something spiral, like a corkscrew.” — Rosa

        Edge Cases:
            In:
                Instructions or corrections about work behavior if tied to a specific case or policing task.

            Out:
                General workplace banter -> conversation_glue
                Emotional reactions to work -> emotion




    Category 2: Food

        Definition:
            Lines focused on describing, offering, evaluating, or obsessing over food, ingredients, meals, snacks, or food-related events.

        Examples (in):
            - “Check out these doughnuts.” — Charles
            - “That’s the best pie I’ve ever had.” — Charles
            - “Everything’s spoiled. My chicken, my potatoes, my pasta, my meatballs…” — Terry
            - “My muffin, my head, my muffin!” — Charles

        Edge Cases:
            In:
                Food used as a metaphor or joke.

            Out:
                Restaurants mentioned only as locations (context-dependent)




    Category 3: Personal Life

        Definition:
            Lines about family, childhood, partners, hobbies, personal interests, insecurities, daily life, or non-work commitments.

        Examples (in):
            - “My twins are learning to walk — chaos reigns at the Jeffords household.” — Terry
            - “Brian was adopted, so he has abandonment issues.” — Charles
            - “I got kicked out of ballet school for beating the crap out of ballerinas.” — Rosa
            - “I’m building this dollhouse for my girls.” — Terry

        Edge Cases:
            In:
                Personal anecdotes even when mentioned at work.

            Out:
                Romantic/sexual lines -> romance
                Emotional venting -> emotion




    Category 4: Emotion

        Definition:
            Lines expressing internal states such as frustration, excitement, fear, guilt, affection, anger, pride, panic, or confidence.

        Examples (in):
            - “I think I'm ready. I'm no longer fixating on my fears.” — Terry
            - “That’s never happened before. I don’t like it.” — Rosa
            - “I’m lost. The universe is a cruel and vexing puzzle.” — Charles
            - “Everything’s spoiled. My lunch is ruined.” — Terry

        Edge Cases:
            In:
                Emotional reactions tied to food, work, or people.

            Out:
                Snarky or biting expressions -> insult_snark
                Romance-related feelings -> romance




    Category 5: Romance

        Definition:
            Lines referencing dating, attraction, romantic feelings, sexual innuendo, flirtation, or discussions of romantic partners.

        Examples (in):
            - “I want to ask Rosa to the Rihanna concert with me.” — Charles
            - “He’s into me.” — Rosa
            - “Oh, my boyfriend’s coming too.” — Rosa
            - “Okay, let’s do this. I think you’re sweet—” — Rosa

        Edge Cases:
            In:
                Crushes, flirtation, jealousy.

            Out:
                Friendly interactions -> conversation_glue
                Compliments with no romantic intent -> context-dependent




    Category 6: Insult / Snark

        Definition:
            Lines that include insults, sarcasm, snippy comments, threats, intimidation, or mocking tones typical of Rosa’s style (and sometimes Terry).

        Examples (in):
            - “You tell anyone, I break your face.” — Rosa
            - “Extinguisher’s empty, morons.” — Rosa
            - “Ignorant and wrong.” — Rosa
            - “Don’t lie to me, Boyle, or you’ll be eating your bone marrow custard through a straw.” — Terry

        Edge Cases:
            In:
                Playful insults between friends.

            Out:
                Legit emotional anger -> emotion
                Loving sarcasm in romantic context -> romance




    Category 7: Conversation Glue

        Definition:
            Short, non-substantive utterances that maintain flow but do not contribute meaning: acknowledgments, simple reactions, filler, quick pivots, affirmations, or agreement lines.

        Examples (in):
            - “Yeah.” / “Yup.” — Rosa
            - “Sure.” — Charles
            - “Got it.” — Terry
            - “Really?” — Charles
            - “What?” — Rosa
            - “Whoo!” — Terry

        Edge Cases:
            In:
                Lines that serve only to keep the scene moving.

            Out:
                Very short but meaningful lines (“No, I can fix this,” “Hands on your head!”) -> another category