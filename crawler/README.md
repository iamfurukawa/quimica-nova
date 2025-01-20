Para criar env:
 - python3 -m venv env

Para ativar o env em:
 - Linux/macOS: source env/bin/activate

Para salvar o estado do env:
 - pip freeze > requirements.txt

Para desativar o env:
 - deactivate



Instalação do teressact
 - brew install tesseract

 
# Count files with download link on database
select count(1) from artigos where pdf_link is not null
Result: 7182

# Count files with .pdf
find articles/ -type f -name "*.pdf" | wc -l 
Result: 7152

# Collect file names without extension
find articles/ -type f -name "*.pdf" -exec basename {} .pdf \; | sed "s/^/'/;s/$/'/" | paste -sd, -

30 files missing:
055ca0fe-0bbc-4ba8-9f4a-f7bb398efc7d
0fe125c6-8640-4aba-9346-4da907a4a83a
118c50dc-0708-463c-9979-ee71b2b6168d
123cc842-83cc-451d-972f-c458ecd3fdef
1c82137e-1743-4bc1-9f47-e1619dfb4c4c
2145c26a-f55e-4823-82b3-3d9671858a09
2c19c365-d318-45d6-b1cf-deaaaa6c2d18
2c6c00e0-0641-4f6d-95de-53e28dd242f1
3a6b3219-c970-4011-9653-2d0ab51e1258
3d6dbf78-ba5c-4a28-8890-9d8d48456ef6
4c03a68a-6337-4e1d-b923-28cd2eb5b4dd
4e5c98a0-aaea-4b50-84c7-7df190646bc1
6370eeb7-fb2a-4f25-8092-1b95aaa347be
749bf91d-6cc4-4da6-8514-fab062248609
7d86034f-2bba-446f-bd33-f960a30fbfd0
800bcf1b-3655-4bc0-aaed-f60545c8c464
962a469e-22ba-4a12-9687-1d9b255e415b
98ae6cbd-b4b7-46b0-9ea8-0dce294d87a9
993e7743-ae7b-49ed-80e6-148895793d57
a50873c2-9ab9-4487-8f5a-e7ad2ac36975
a635cfc5-302d-49c2-b794-10178beee712
ace1aa9d-ce26-4fb3-b10f-9e588443169d
b5aff0d3-4cfb-457e-b4c8-9ac74c8ca2e4
bb4a8e82-ccbb-48ff-adf0-a8e48b5823a8
cfb3a16c-dddc-4e4b-b41a-42f34ef45983
db9848ff-014b-4560-a001-a55259893963
eb74a930-67cb-46f9-b53d-6e28916041f8
eeb57246-abf9-49e2-b77e-46c11b1b703a
f1b2d90e-0a40-4c27-b644-3c78f6641f9a
fe3bef61-b01d-47ab-a847-47835afd655c

Reason: Access Denied

# Remove files with .md
find articles/ -type f -name "*.md" -exec rm -f {} +
