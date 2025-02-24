import os
import datetime
import git
import schedule
import time

# CECI EST UN SCRIPT OPEN SOURCE REDIGE PAR CHAMALHAT

# Chemin vers votre dépôt local
REPO_PATH = '/Users/votre-nom-utilisateur/Documents/votre-depot'

def commit_changes():
    try:
        # Ouvrir le dépôt
        repo = git.Repo(REPO_PATH)

        # Vérifier s'il y a des modifications (s'il n'y en a pas, il n'y aura aucun commit)
        if repo.is_dirty(untracked_files=True):
            # Ajouter tous les fichiers modifiés
            repo.git.add(A=True)

            # Effectuer le commit
            commit_message = f'Commit automatique du {datetime.datetime.now().strftime("%Y-%m-%d")}'
            repo.index.commit(commit_message)

            # Pousser les modifications vers le dépôt distant
            origin = repo.remote(name='origin')
            origin.push()

            print(f'Commit et push effectués avec succès : {commit_message}')
        else:
            print('Aucune modification à commiter.')
    except Exception as e:
        print(f'Erreur lors du commit : {e}')

# Planifier le commit quotidien à minuit (à modifier selon besoin ou ajouter d'autres horaires)
schedule.every().day.at('00:00').do(commit_changes)

print('Script de commit automatique démarré.')

# Boucle principale pour exécuter les tâches planifiées
while True:
    schedule.run_pending()
    time.sleep(1)
