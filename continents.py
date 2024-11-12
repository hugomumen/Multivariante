continent_dict = {
    # África
    'Angola': 'Africa', 'Argelia': 'Africa', 'Benín': 'Africa', 'Botsuana': 'Africa',
    'Burkina Faso': 'Africa', 'Burundi': 'Africa', 'Cabo Verde': 'Africa', 'Camerún': 'Africa',
    'Chad': 'Africa', 'Comoras': 'Africa', 'República del Congo': 'Africa',
    'República Democrática del Congo': 'Africa', 'Costa de Marfil': 'Africa', 'Egipto': 'Africa',
    'Eritrea': 'Africa', 'Etiopía': 'Africa', 'Gabón': 'Africa', 'Gambia': 'Africa', 'Ghana': 'Africa',
    'Guinea': 'Africa', 'Guinea Ecuatorial': 'Africa', 'Guinea-Bissau': 'Africa',
    'Kenia': 'Africa', 'Lesoto': 'Africa', 'Liberia': 'Africa', 'Libia': 'Africa', 'Madagascar': 'Africa',
    'Malaui': 'Africa', 'Malí': 'Africa', 'Marruecos': 'Africa', 'Mauricio': 'Africa', 'Mauritania': 'Africa',
    'Mozambique': 'Africa', 'Namibia': 'Africa', 'Níger': 'Africa', 'Nigeria': 'Africa',
    'República Centroafricana': 'Africa', 'Ruanda': 'Africa', 'Senegal': 'Africa',
    'Seychelles': 'Africa', 'Sierra Leona': 'Africa', 'Somalía': 'Africa', 'Sudáfrica': 'Africa',
    'Sudán': 'Africa', 'Sudán del Sur': 'Africa', 'Suazilandia': 'Africa', 'Tanzania': 'Africa',
    'Togo': 'Africa', 'Túnez': 'Africa', 'Uganda': 'Africa', 'Yibuti': 'Africa', 'Zambia': 'Africa',
    'Zimbabue': 'Africa',

    # América
    'Bermudas': 'America', 'Canadá': 'America', 'Estados Unidos': 'America',
    'Groenlandia': 'America', 'México': 'America', 'San Pedro y Miquelón': 'America',
    'Argentina': 'America', 'Bolivia': 'America', 'Brasil': 'America', 'Chile': 'America',
    'Colombia': 'America', 'Ecuador': 'America', 'Guayana Francesa': 'America', 'Guyana': 'America',
    'Paraguay': 'America', 'Perú': 'America', 'Surinam': 'America', 'Uruguay': 'America',
    'Venezuela': 'America', 'Belice': 'America', 'Costa Rica': 'America', 'El Salvador': 'America',
    'Guatemala': 'America', 'Honduras': 'America', 'Nicaragua': 'America', 'Panamá': 'America',
    'Cuba': 'America', 'República Dominicana': 'America', 'Puerto Rico': 'America', 'Jamaica': 'America',
    'Trinidad y Tobago': 'America', 'Barbados': 'America', 'Bahamas': 'America', 'Haití': 'America',
    'Granada': 'America', 'San Vicente y las Granadinas': 'America', 'Santa Lucía': 'America',
    'San Cristóbal y Nieves': 'America',

    # Asia
    'Afganistán': 'Asia', 'Arabia Saudita': 'Asia', 'Armenia': 'Asia', 'Azerbaiyán': 'Asia',
    'Bangladés': 'Asia', 'Baréin': 'Asia', 'Birmania': 'Asia', 'Bután': 'Asia', 'Brunéi': 'Asia',
    'Camboya': 'Asia', 'Catar': 'Asia', 'China': 'Asia', 'Corea del Norte': 'Asia',
    'Corea del Sur': 'Asia', 'Emiratos Árabes Unidos': 'Asia', 'Filipinas': 'Asia', 'Georgia': 'Asia',
    'India': 'Asia', 'Indonesia': 'Asia', 'Irak': 'Asia', 'Irán': 'Asia', 'Israel': 'Asia',
    'Japón': 'Asia', 'Jordania': 'Asia', 'Kazajistán': 'Asia', 'Kirguistán': 'Asia', 'Kuwait': 'Asia',
    'Laos': 'Asia', 'Líbano': 'Asia', 'Malasia': 'Asia', 'Maldivas': 'Asia', 'Mongolia': 'Asia',
    'Nepal': 'Asia', 'Omán': 'Asia', 'Pakistán': 'Asia', 'Palestina': 'Asia', 'Rusia': 'Asia',
    'Singapur': 'Asia', 'Siria': 'Asia', 'Sri Lanka': 'Asia', 'Tailandia': 'Asia', 'Tayikistán': 'Asia',
    'Turkmenistán': 'Asia', 'Turquía': 'Asia', 'Uzbekistán': 'Asia', 'Vietnam': 'Asia', 'Yemen': 'Asia',

    # Europa
    'Albania': 'Europe', 'Alemania': 'Europe', 'Andorra': 'Europe', 'Austria': 'Europe',
    'Bélgica': 'Europe', 'Bielorrusia': 'Europe', 'Bosnia y Herzegovina': 'Europe', 'Bulgaria': 'Europe',
    'Chipre': 'Europe', 'Croacia': 'Europe', 'Dinamarca': 'Europe', 'Eslovaquia': 'Europe',
    'Eslovenia': 'Europe', 'España': 'Europe', 'Estonia': 'Europe', 'Finlandia': 'Europe',
    'Francia': 'Europe', 'Grecia': 'Europe', 'Hungría': 'Europe', 'Irlanda': 'Europe', 'Islandia': 'Europe',
    'Italia': 'Europe', 'Kosovo': 'Europe', 'Letonia': 'Europe', 'Liechtenstein': 'Europe',
    'Lituania': 'Europe', 'Luxemburgo': 'Europe', 'Macedonia del Norte': 'Europe', 'Malta': 'Europe',
    'Moldavia': 'Europe', 'Noruega': 'Europe', 'Países Bajos': 'Europe', 'Polonia': 'Europe',
    'Portugal': 'Europe', 'Reino Unido': 'Europe', 'República Checa': 'Europe', 'Rumania': 'Europe',
    'San Marino': 'Europe', 'Serbia': 'Europe', 'Suecia': 'Europe', 'Suiza': 'Europe', 'Ucrania': 'Europe',

    # Oceanía
    'Australia': 'Oceania', 'Fiyi': 'Oceania', 'Islas Cook': 'Oceania', 'Islas Marshall': 'Oceania',
    'Islas Salomón': 'Oceania', 'Micronesia': 'Oceania', 'Nauru': 'Oceania', 'Nueva Zelanda': 'Oceania',
    'Palaos': 'Oceania', 'Papúa Nueva Guinea': 'Oceania', 'Samoa': 'Oceania', 'Tonga': 'Oceania',
    'Tuvalu': 'Oceania', 'Vanuatu': 'Oceania'
}