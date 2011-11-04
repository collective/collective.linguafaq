I18NDUDE = i18ndude
I18NDOMAIN = collective.linguafaq

default:help
	@echo "-------------------------------------------------------------------"
	@echo "Nothing to be done by default."
	@echo "-------------------------------------------------------------------"

help:
	@echo "-------------------------------------------------------------------"
	@echo "MANUAL"
	@echo "pot             : update potfile"
	@echo "sync lang=XX    : sync .po-file for language XX"
	@echo "compile lang=XX : compile .mo-file for language XX"
	@echo "-------------------------------------------------------------------"

pot:
	@echo "-------------------------------------------------------------------"
	@echo "Generating potfile..."
	${I18NDUDE} rebuild-pot --pot ${I18NDOMAIN}.pot --create ${I18NDOMAIN} ../
	@echo "-------------------------------------------------------------------"

sync:
	@echo "-------------------------------------------------------------------"
	@if [ -z $(lang) ]; \
	then echo "No language specified";\
	else echo "Syncing language $(lang)";\
	${I18NDUDE} sync --pot ${I18NDOMAIN}.pot $(lang)/LC_MESSAGES/${I18NDOMAIN}.po;\
	fi
	@echo "-------------------------------------------------------------------"

compile:
	@echo "-------------------------------------------------------------------"
	msgfmt -o $(lang)/LC_MESSAGES/${I18NDOMAIN}.mo $(lang)/LC_MESSAGES/${I18NDOMAIN}.po
	@echo "-------------------------------------------------------------------"

