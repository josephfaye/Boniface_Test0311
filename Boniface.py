
import random

def poser_question(question, choix):
    print(question)
    for i, option in enumerate(choix, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            reponse_utilisateur = int(input("Votre réponse (entrez le numéro correspondant) : "))
            if 1 <= reponse_utilisateur <= len(choix):
                return reponse_utilisateur
            else:
                print("Veuillez entrer un numéro valide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

def jouer_quiz(questions):
    score = 0
    random.shuffle(questions)
    
    for q in questions:
        reponse_utilisateur = poser_question(q["question"], q["choix"])
        
        if reponse_utilisateur == q["reponse"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! La réponse correcte était {q['reponse']}: {q['choix'][q['reponse']-1]}\n")
    
    print(f"Score final : {score}/{len(questions)}")

if __name__ == "__main__":
    questions_quiz = [
        {
            "question": "Quelle est la capitale de la France?",
            "choix": ["Paris", "Berlin", "Londres", "Madrid"],
            "reponse": 1
        },
        {
            "question": "Quelle est la plus grande planète du système solaire?",
            "choix": ["Vénus", "Mars", "Jupiter", "Saturne"],
            "reponse": 3
        },
        {
            "question": "Quelle est la couleur du ciel par temps clair?",
            "choix": ["Rouge", "Vert", "Bleu", "Jaune"],
            "reponse": 3
        },
        
    ]

    jouer_quiz(questions_quiz)
