# Import Python's random module
init python:
    import random

# Declare the characters
define a = Character("Aarav", color="#3498db")
define m = Character("Magistrate", color="#f8c471")
define c = Character("Contractor Dhokle", color="#e74c3c")
define w = Character("Worker", color="#2ecc71")
define e = Character("Electrician", color="#9b59b6")

# Default variables
default cement_checked = False
default rods_checked = False
default rods_pass_test = True  # Randomized later
default bribe_taken = False
default wires_checked = False

# Start the game
label start:

    # Prologue: The Assignment
    scene bg office
    "In a government office in the Jabalpur district of MP..."
    show magistrate normal

    m "Aarav, this isn’t just another project. This school in Jamunia village will serve hundreds of underprivileged children. It’s not just bricks and mortar—it’s hope for the future."

    show magistrate normal at left with move

    show aarav casualnormal at right

    a "I understand, ma’am. I’ll ensure it’s built to the highest standards."

    m "The budget is tight, and the monsoons are just months away. You’ll need to be resourceful without compromising quality."

    " Aarav took the blueprint handed to him, examining the design of the school: four classrooms, a small library, and a playground."

    m  "One more thing, Aarav. Keep an eye out for compliance with BIS standards. Too many shortcuts have been taken in rural projects lately, and it’s cost lives."

    show aarav casualsmile
    a "I’ll make sure every material we use meets BIS certification. The safety of those kids comes first."

    show magistrate smile

    m "Good luck, Aarav. Jamunia is counting on you."

    jump cement_gamble

# Chapter 1: The Cement Gamble
label cement_gamble:

    scene bg site with fade
    "Aarav reaches the school site to meet Contractor Dhokle."
    show aarav normal

    a "What cement are we going to use?"
    show aarav normal at left with move
    show contractor normal at right
    c "Sir, we have two choices: Brand A (ISI-certified) and Brand B (cheaper, non-certified)."

    a "What’s the difference between the two?"

    c "Sir, one is ISI-certified, and the other isn’t. But believe me, they work the same. You’ll save ₹2 lakhs easily if we go with the non-certified one."

    a " (Thinking) We definitely are on a tight budget, should i consider this offer."

    menu:
        "Demand ISI-marked cement":
            $ cement_checked = True
            a "Safety comes first. We will use ISI-marked cement only. Let me check the ISI mark of the cement you’re suggesting."
            show contractor sad
            c "As you wish, sir."
            "Aarav checks the CM/L number on the cement and finds that it is ISI certified."

        "Accept the deal and take a percentage of the profit":
            $ cement_checked = False
            a "We’re running out of funds. Let’s go with your plan."
            show contractor smile
            c "Sure, sir. We’ll make great profits together."

    jump steel_rod_sabotage

# Chapter 2: Steel Rod Sabotage
label steel_rod_sabotage:

    scene bg site with fade
    "Few days later, a worker approaches Aarav."
    show worker shocked at left
    show aarav normal at right

    w "These rods snap like twigs, sir. Have they been ISI-certified?"
    show worker sad
    a "I’ll talk to the contractor about this."

    scene bg site with fade
    show aarav shocked
    a "I’ve been hearing complaints about the rods breaking easily. You told me they were ISI-certified. Then what is this?"
    show aarav normal at left with move
    show contractor angry at right
    c "Sir, they are ISI-certified. Must be the fault of those workers."

    menu:
        "Send rods for lab tests":
            $ rods_checked = True
            a "I will send some samples for lab testing to make sure you aren’t lying."
            scene bg lab with fade
            "(The lab testing of rods is conducted.)"
            
            scene bg chemical1 with fade
            "Chemical Test"
            scene bg chemical2
            "Determination of the percentage of key elements like carbon, sulfur, phosphorus, manganese, etc., using spectrometry or wet chemical methods (as per IS 228)."
            "The chemical composition must conform to specified limits, ensuring weldability and preventing brittleness or corrosion."

            scene bg tensile_test1 with fade
            "Tensile Test"
            "Determines yield stress (minimum stress to deform the rod), ultimate tensile strength, and elongation."
            scene bg tensile_test2
            "Conducted using a universal testing machine in accordance with IS 1608 and IS 2062. The rod is subjected to increasing tension until it breaks."
            "The results are compared with the minimum standards for different grades (e.g., Fe 415, Fe 500, Fe 550, Fe 600)."

            scene bg bendtest1 with fade
            "Bend Test"
            "Evaluates the ductility and ability of the rod to withstand bending without cracking."
            scene bg bendtest2
            "The rod is bent over a mandrel with a specific diameter based on its size and grade."
            "After bending, the rod is inspected for any cracks or ruptures. If no cracks are visible, the rod passes the test."

            scene bg rebendtest1 with fade
            "Re-Bend Test"
            "Assesses the resistance of the rod to cracks under repeated bending and its aging behavior."
            scene bg rebendtest2
            "The rod is first bent to an angle of 135° over a mandrel and then placed in boiling water (100°C) for 30 minutes."
            scene bg rebendtest3
            "After cooling, it is bent back to 157.5°. If no cracks appear in the bent portion, the rod passes this test."

            scene bg pullout1 with fade
            "Pull Out Test"
            "Conducted to verify the bonding properties of deformed bars with concrete."
            scene bg pullout2
            "The bond strength is calculated using the load required to achieve specific levels of slip (e.g., 0.025 mm and 0.25 mm)."
            "Bars must exceed the bond strength of plain round bars of the same size by at least 40 and 80 percent, respectively."

            $ rods_pass_test = random.choice([True, False])

            if rods_pass_test:
                scene bg site with fade
                "A report of the lab test is sent back to Aarav."
                show aarav casualsad at left
                show contractor smile at right
                a "Rods passed the lab test. They adhere to IS 1786 standards. Sorry for doubting you."
                c "I told you, sir. It must be the worker’s fault."
                jump electrical_wiring
            else:
                scene bg site with fade
                "A report of the lab test is sent back to Aarav."
                show aarav casualangry at left
                show contractor sad at right
                a "The rods failed the test. They’re not up to IS 1786 standards. I’m getting you fired."
                c "I’m sorry, sir. This won’t happen again."
                jump contractor_bribe

        "Believe the contractor":
            $ rods_checked = False
            a "I think you’re right. It must be the workers."
            show contractor smile
            c "Exactly, sir."
            jump electrical_wiring

# Chapter 2.1: The Contractor’s Bribe
label contractor_bribe:

    scene bg office_night with fade
    "Later that night, contractor Dhokle came to meet Aarav."
    show aarav casualnormal
    a "Why are you here Mr. Dhokle?"
    show aarav casualnormal at left with move
    show contractor casualsad at right
    c "I want to fix the rod issue."
    a "And how are you planning to do this?"
    c "Aarav, let’s keep this between us. ₹1 lakh to ignore the rod issue. No one will know."

    menu:
        "Report contractor Dhokle to the police":
            $ bribe_taken = False
            show aarav casualangry
            a "Bribery won’t fix a broken structure. I’m reporting this to the police."
            c "No sir, please don't."
            scene bg police with fade
            show contractor casualsad
            "(Contractor Dhokle is arrested for bribery and fraud.)"
            return

        "Accept the bribe":
            $ bribe_taken = True
            show aarav casualkapti
            a "(Sighs) Fine, give me the money."
            show contractor casualsmile
            c "Thank you, sir. It’s great working with you."

    jump electrical_wiring

# Chapter 3: Electrical Wiring Danger
label electrical_wiring:

    scene bg classroom
    "While inspecting the classrooms, Aarav notices the electrician with the wires."
    show aarav normal

    a "These wires look thin. Are they ISI-marked?"
    show aarav normal at left with move
    show electrician normal at right
    e "No, sir. These wires are imported from China."

    show aarav shocked

    a "But that can cause a fire in case of power surges. Why aren’t we using ISI marked wires?"

    show electrician kapat

    e "They’re cheaper than the ISI ones and work just as well! You can trust me on this, these also fit easily in our budget."

    menu:
        "Reject and order ISI wires:":
            $ wires_checked = True
            a "No shortcuts. Overloaded wires can cause fires. I’ll cover the cost from my salary if needed. We must get cables with IS 1554 and IS 694 standards."
            show electrician shocked
            e "As you wish, sir."

        "Approve the cheap wires:":
            $ wires_checked = False
            show aarav normal
            a "Okay, we can’t afford delays anyway. Just get the job done quickly."
            show electrician smile
            e "Sure sir."

    scene bg school with fade
    "The contruction of the school is completed in a few weeks."

    jump monsoon_test

# Chapter 4: The Monsoon Test
label monsoon_test:

    scene bg school

    "A few weeks later the first heavy rains lash the village. The villagers anxiously watch the school building."

    if cement_checked and rods_checked and rods_pass_test and wires_checked:
        "The school stands tall, with no signs of damage. Villagers cheer and celebrate Aarav."
        scene bg office with fade

        show magistrate smile
        m "We are proud of you Aarav, you managed to build a school on such a tight budget without compromising on its strength and stability."
        show magistrate smile at left with move
        show aarav casualsmile at right
        a "Thank You so much ma’am, it was my duty."
        m "I will definitely talk about your promotion to your seniors."
        a "(Smiles)"

    elif not cement_checked and (not rods_checked or (not rods_pass_test and bribe_taken)) and not wires_checked:
        scene bg school_broken with fade
        "The roof collapses even before the school starts. The villagers are angry and Aarav is summoned at the Magistrate's Office"
        scene bg office with fade
        
        show magistrate dissapointed
        m "Aarav, I trusted you with this project. The school hasn’t even opened, and the roof has already collapsed!...{w} This wasn’t just a building—it was supposed to be a beacon of hope for those children!"
        show magistrate dissapointed at left with move
        show aarav casualdistressed at right
        a "Ma’am, I… I didn’t think it would come to this. The budget… the pressure…"
        show magistrate angry
        m "Don’t you DARE blame the budget! This isn’t about money—it’s about integrity! You ignored every warning, every red flag, all for what? Saving a few lakhs and lining your pockets?"
        a "I didn’t mean for this to happen. I just…"
        m "Intentions don’t matter when lives are at stake! This report is damning, Aarav. Substandard cement, brittle rods, faulty wiring… everything screams negligence and corruption... {w} You’ve not just failed as an engineer—you’ve failed as a human being."
        a "I am really sorry ma'am..."
        m "You’ll answer for this in court. And don’t think for a second that I’ll protect you. The Bureau of Indian Standards is already involved. I hope you’re ready to face the consequences."
        scene bg police with fade
        show aarav casualsad
        if bribe_taken:
            "Aarav faces charges for endangering life of others, later the investigating committee discover corruption angles in the case."
            "Aarav loses his job and suffers imprisonment for his acts."
        else:
            "Aarav faces charges for endangering life of others, faces fines and imprisonment."
    else:
        scene bg school_crack with fade
        "The walls develop cracks even before the first session starting at the school, the villagers remain distrustful of the building. Aarav is summoned at the Magistrate's Office"
        scene bg office with fade
        
        show magistrate dissapointed
        m "Aarav, do you realize how much faith we put in you? Aarav, the school wasn’t even operational, and it’s already showing cracks. This was supposed to be a beacon of hope for the village, and now it’s a structure they can’t trust!"
        show magistrate dissapointed at left with move
        show aarav casualdistressed at right
        a "Ma’am, the cracks are superficial. The structure is still safe—"
        show magistrate angry
        m "Safe? Do you think parents will send their children into a building with visible cracks? You didn’t just fail them—you’ve humiliated this office. What happened to the BIS compliance you promised me?"
        a "I… I inspected the materials, but I might have overlooked the curing process or the foundation quality during the rush to meet deadlines."
        m "Deadlines? Is that your excuse for negligence? What about the BIS standards? Were they even followed?"
        a "The materials were marked, but I didn’t cross-check everything thoroughly…"
        m "This isn’t about one mistake, Aarav. The villagers have lost faith in us. You’ve embarrassed the administration. Consider yourself lucky this didn’t end in a disaster."
        a "I am really sorry ma'am..."
        m "You’ll face an inquiry. Until then, I don’t want to hear excuses. Fix this mess and pray the cracks in the walls don’t mirror the cracks in your career!"
        scene bg office with fade
        show aarav casualsad
        "Chargesheets are filed against Aarav and he loses his reputation."

    return
