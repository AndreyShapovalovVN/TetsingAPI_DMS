# Description: Test data for query tests
QUERY_POSITIVE = [
    {
        'IdentCode': '455340242',
        'UniqueCode': '19730924-00018',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
        'Gender': 'ч',
        'DocSeries': None,
        'DocNumber': '19730924-00018',
        'DocType': 2
    },
    {
        'IdentCode': '455340242',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
        'Gender': 'ч',
        'DocSeries': None,
        'DocNumber': '19730924-00018',
        'DocType': 2
    },
    {
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
        'DocSeries': None,
        'DocNumber': '19730924-00018',
        'DocType': 2
    },
    {
        'IdentCode': '455340242',
        'UniqueCode': '19730924-00018',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
    },
    {
        'IdentCode': '455340242',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
    },
    {
        'UniqueCode': '19730924-00018',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
    },
    {
        'IdentCode': '9999999999',
        'UniqueCode': '19730924-00018',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DocSeries': None,
        'DocNumber': '19730924-99999',
        'DateBirth': '1973-09-24',
        'DocType': 2
    },
    {
        'IdentCode': '9999999999',
        'UniqueCode': '19730924-99999',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DocSeries': None,
        'DocNumber': '19730924-00018',
        'DocType': 2,
        'DateBirth': '1973-09-24',
    },
    {
        'IdentCode': '455340242',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-23',
    },
    {
        'IdentCode': '455340242',
        'LastName': 'ЛЮБИШ',
        'FirstName': 'ОЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
    },
    {
        'IdentCode': '455340242',
        'LastName': 'ЛЮБИШ',
        'FirstName': 'ОЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-23',
    },
    {
        'IdentCode': '455340242',
        'LastName': 'ЛЮБИШЬ',
        'FirstName': 'ОЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-23',
    },
    {
        'IdentCode': '455340242',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-08-23',
    },
]

QUERY_NEGATIVE = [
    {
        'IdentCode': '455340242',
        'LastName': 'ЛЮБИШЬ',
        'FirstName': 'AЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-23',
    },
    {
        'IdentCode': '455340242',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1974-08-23',
    },

]

QUERY_NEGATIVE_404 = [
    {
        'IdentCode': '9999999999',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
    },
{
        'UniqueCode': '19730924-99999',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
    },
{
        'IdentCode': '9999999999',
        'UniqueCode': '19730924-99999',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
    },
    {
        'IdentCode': '9999999999',
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
        'DocSeries': None,
        'DocNumber': '19730924-99999',
        'DocType': 2
    },
    {
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
        'DocSeries': None,
        'DocNumber': '19730924-99999',
        'DocType': 2
    },
    {
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
        'DocSeries': None,
        'DocNumber': '19730924-00018',
        'DocType': 1
    },
    {
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
        'DocSeries': None,
        'DocNumber': '19730924-00018',
        'DocType': 0
    },
    {
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
        'DocSeries': None,
        'DocNumber': '19730924-00018',
        'DocType': 3
    },
    {
        'LastName': 'ЛЮБІШ',
        'FirstName': 'ОЛЛЕКСАНДР',
        'Patronymic': 'ПАРГЕВОВИЧ',
        'DateBirth': '1973-09-24',
        'DocSeries': 'АА',
        'DocNumber': '19730924-00018',
        'DocType': 2
    },
]