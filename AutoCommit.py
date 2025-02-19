import os
import datetime
import git
import schedule
import time

# Chemin vers votre dépôt local
REPO_PATH = '/Users/jordandefay/Documents/school-test'

def commit_changes():
    try:
        # Ouvrir le dépôt
        repo = git.Repo(REPO_PATH)

        # Vérifier s'il y a des modifications
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

# Planifier le commit quotidien à minuit
schedule.every().day.at('23:59').do(commit_changes)

print('Script de commit automatique démarré.')

# Boucle principale pour exécuter les tâches planifiées
while True:
    schedule.run_pending()
    time.sleep(1)
