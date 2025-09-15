Vérifie la qualité d’une flashcard par rapport à l’extrait fourni.
Retourne un JSON { "keep": true|false, "reason": "...", "fix": "..." }
Critères: répondable depuis l’extrait, non ambiguë, niveau pertinent, pas de hors-sujet.
Si "keep" = false mais réparable, propose "fix".
