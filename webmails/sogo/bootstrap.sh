#!/bin/sh

set -e

# check to make sure there is a .sql file specified to import
if [ ! -f /etc/sogo/mysql.conf ] || [ ! -f /etc/sogo/boostrap.sql ]
then
  echo "/etc/sogo/mysql.conf or /etc/sogo/boostrap.sql is not found; exiting"
  exit 1
fi

source /etc/sogo/mysql.conf

# check to make sure the db is accessible before importing data
while [ $(mysql --connect-timeout=1 ${MYSQL_OPTIONS} -e "show databases;" > /dev/null 2>&1; echo $?) -ne 0 ]
do
  echo "Unable to connect to MySQL, retrying..."
  sleep 2
done

echo -e "\nMySQL is now accessible"'!'"\n"

echo "Pre import databases:"
mysql -t ${MYSQL_OPTIONS} -e "show databases;" 2> /dev/null

echo -e "\nImporting bootstrap.sql..."
mysql ${MYSQL_OPTIONS} < /etc/sogo/bootstrap.sql 2> /dev/null
echo -e "Import complete"'!'"\n"

echo "Post import databases:"
mysql -t ${MYSQL_OPTIONS} -e "show databases;" 2> /dev/null

echo -e "\nDatabase bootstrap complete"'!'

exec "$@"
