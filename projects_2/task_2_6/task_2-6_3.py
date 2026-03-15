phenotype_donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
phenotype_patient = input("Введите фенотип группы крови пациента (I, II, III, IV): ").strip().upper()
if phenotype_donor == phenotype_patient or phenotype_donor == "I":
    print("Переливание возможно")
else:
    print("Не рекомендовано переливание")