Banco de dados Postgre usando docker:
docker run --name postgres -e POSTGRES_USER=iamfurukawa -e POSTGRES_PASSWORD=1234 -e POSTGRES_DB=quimica-nova -p 5432:5432 -d postgres