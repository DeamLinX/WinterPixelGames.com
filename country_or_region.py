from common_config import set_localization


def country_region(selected_language, flag_emoji=None):
    _ = set_localization(selected_language)

    country_region_dict = {
        "🌐": _("Global"),
        "🇦🇫": _("Afghanistan"),
        "🇦🇱": _("Albania"),
        "🇩🇿": _("Algeria"),
        "🇼🇸": _("American Samoa"),
        "🇦🇩": _("Andorra"),
        "🇦🇴": _("Angola"),
        "🇦🇮": _("Anguilla"),
        "🇦🇬": _("Antigua and Barbuda"),
        "🇦🇷": _("Argentina"),
        "🇦🇲": _("Armenia"),
        "🇦🇼": _("Aruba"),
        "🇦🇺": _("Australia"),
        "🇦🇹": _("Austria"),
        "🇦🇿": _("Azerbaijan"),
        "🇧🇸": _("Bahamas"),
        "🇧🇭": _("Bahrain"),
        "🇧🇩": _("Bangladesh"),
        "🇧🇧": _("Barbados"),
        "🇧🇾": _("Belarus"),
        "🇧🇪": _("Belgium"),
        "🇧🇿": _("Belize"),
        "🇧🇯": _("Benin"),
        "🇧🇲": _("Bermuda"),
        "🇧🇹": _("Bhutan"),
        "🇧🇴": _("Bolivia"),
        "🇧🇦": _("Bosnia and Herzegovina"),
        "🇧🇼": _("Botswana"),
        "🇧🇻": _("Bouvet Island"),
        "🇧🇷": _("Brazil"),
        "🇮🇴": _("British Indian Ocean Territory"),
        "🇧🇳": _("Brunei Darussalam"),
        "🇧🇬": _("Bulgaria"),
        "🇧🇫": _("Burkina Faso"),
        "🇧🇮": _("Burundi"),
        "🇰🇭": _("Cambodia"),
        "🇨🇲": _("Cameroon"),
        "🇨🇦": _("Canada"),
        "🇨🇻": _("Cape Verde"),
        "🇰🇾": _("Cayman Islands"),
        "🇨🇫": _("Central African Republic"),
        "🇹🇩": _("Chad"),
        "🇨🇱": _("Chile"),
        "🇨🇳": _("China"),
        "🇨🇽": _("Christmas Island"),
        "🇨🇨": _("Cocos (Keeling) Islands"),
        "🇨🇴": _("Colombia"),
        "🇰🇲": _("Comoros"),
        "🇨🇬": _("Congo"),
        "🇨🇩": _("Congo, the Democratic Republic of the"),
        "🇨🇰": _("Cook Islands"),
        "🇨🇷": _("Costa Rica"),
        "🇭🇷": _("Croatia"),
        "🇨🇺": _("Cuba"),
        "🇨🇼": _("Curaçao"),
        "🇨🇾": _("Cyprus"),
        "🇨🇿": _("Czech Republic"),
        "🇨🇮": _("Côte d'Ivoire"),
        "🇩🇰": _("Denmark"),
        "🇩🇯": _("Djibouti"),
        "🇩🇲": _("Dominica"),
        "🇩🇴": _("Dominican Republic"),
        "🇪🇨": _("Ecuador"),
        "🇪🇬": _("Egypt"),
        "🇸🇻": _("El Salvador"),
        "🇬🇶": _("Equatorial Guinea"),
        "🇪🇷": _("Eritrea"),
        "🇪🇪": _("Estonia"),
        "🇪🇹": _("Ethiopia"),
        "🇫🇰": _("Falkland Islands (Malvinas)"),
        "🇫🇴": _("Faroe Islands"),
        "🇫🇯": _("Fiji"),
        "🇫🇮": _("Finland"),
        "🇫🇷": _("France"),
        "🇬🇫": _("French Guiana"),
        "🇵🇫": _("French Polynesia"),
        "🇹🇫": _("French Southern Territories"),
        "🇬🇦": _("Gabon"),
        "🇬🇲": _("Gambia"),
        "🇬🇪": _("Georgia"),
        "🇩🇪": _("Germany"),
        "🇬🇭": _("Ghana"),
        "🇬🇮": _("Gibraltar"),
        "🇬🇷": _("Greece"),
        "🇬🇱": _("Greenland"),
        "🇬🇩": _("Grenada"),
        "🇬🇵": _("Guadeloupe"),
        "🇬🇺": _("Guam"),
        "🇬🇹": _("Guatemala"),
        "🇬🇬": _("Guernsey"),
        "🇬🇳": _("Guinea"),
        "🇬🇼": _("Guinea-Bissau"),
        "🇬🇾": _("Guyana"),
        "🇭🇹": _("Haiti"),
        "🇭🇲": _("Heard Island and Mcdonald Islands"),
        "🇭🇳": _("Honduras"),
        "🇭🇰": _("Hong Kong"),
        "🇭🇺": _("Hungary"),
        "🇮🇸": _("Iceland"),
        "🇮🇳": _("India"),
        "🇮🇩": _("Indonesia"),
        "🇮🇷": _("Iran"),
        "🇮🇶": _("Iraq"),
        "🇮🇪": _("Ireland"),
        "🇮🇲": _("Isle of Man"),
        "🇮🇱": _("Israel"),
        "🇮🇹": _("Italy"),
        "🇯🇲": _("Jamaica"),
        "🇯🇵": _("Japan"),
        "🇯🇪": _("Jersey"),
        "🇯🇴": _("Jordan"),
        "🇰🇿": _("Kazakhstan"),
        "🇰🇪": _("Kenya"),
        "🇰🇮": _("Kiribati"),
        "🇽🇰": _("Kosovo"),
        "🇰🇼": _("Kuwait"),
        "🇰🇬": _("Kyrgyzstan"),
        "🇱🇦": _("Lao People's Democratic Republic"),
        "🇱🇻": _("Latvia"),
        "🇱🇧": _("Lebanon"),
        "🇱🇸": _("Lesotho"),
        "🇱🇷": _("Liberia"),
        "🇱🇾": _("Libya"),
        "🇱🇮": _("Liechtenstein"),
        "🇱🇹": _("Lithuania"),
        "🇱🇺": _("Luxembourg"),
        "🇲🇴": _("Macao"),
        "🇲🇰": _("Macedonia"),
        "🇲🇬": _("Madagascar"),
        "🇲🇼": _("Malawi"),
        "🇲🇾": _("Malaysia"),
        "🇲🇻": _("Maldives"),
        "🇲🇱": _("Mali"),
        "🇲🇹": _("Malta"),
        "🇲🇭": _("Marshall Islands"),
        "🇲🇶": _("Martinique"),
        "🇲🇷": _("Mauritania"),
        "🇲🇺": _("Mauritius"),
        "🇾🇹": _("Mayotte"),
        "🇲🇽": _("Mexico"),
        "🇫🇲": _("Micronesia"),
        "🇲🇩": _("Moldova"),
        "🇲🇨": _("Monaco"),
        "🇲🇳": _("Mongolia"),
        "🇲🇪": _("Montenegro"),
        "🇲🇸": _("Montserrat"),
        "🇲🇦": _("Morocco"),
        "🇲🇿": _("Mozambique"),
        "🇲🇲": _("Myanmar"),
        "🇳🇦": _("Namibia"),
        "🇳🇷": _("Nauru"),
        "🇳🇵": _("Nepal"),
        "🇳🇱": _("Netherlands"),
        "🇳🇨": _("New Caledonia"),
        "🇳🇿": _("New Zealand"),
        "🇳🇮": _("Nicaragua"),
        "🇳🇪": _("Niger"),
        "🇳🇬": _("Nigeria"),
        "🇳🇺": _("Niue"),
        "🇳🇫": _("Norfolk Island"),
        "🇰🇵": _("North Korea"),
        "🇲🇵": _("Northern Mariana Islands"),
        "🇳🇴": _("Norway"),
        "🇴🇲": _("Oman"),
        "🇵🇰": _("Pakistan"),
        "🇵🇼": _("Palau"),
        "🇵🇸": _("Palestine"),
        "🇵🇦": _("Panama"),
        "🇵🇬": _("Papua New Guinea"),
        "🇵🇾": _("Paraguay"),
        "🇵🇪": _("Peru"),
        "🇵🇭": _("Philippines"),
        "🇵🇳": _("Pitcairn"),
        "🇵🇱": _("Poland"),
        "🇵🇹": _("Portugal"),
        "🇵🇷": _("Puerto Rico"),
        "🇶🇦": _("Qatar"),
        "🇷🇴": _("Romania"),
        "🇷🇺": _("Russia"),
        "🇷🇼": _("Rwanda"),
        "🇷🇪": _("Réunion"),
        "🇧🇱": _("Saint Barthélemy"),
        "🇸🇭": _("Saint Helena, Ascension and Tristan Da Cunha"),
        "🇰🇳": _("Saint Kitts and Nevis"),
        "🇱🇨": _("Saint Lucia"),
        "🇲🇫": _("Saint Martin (French Part)"),
        "🇵🇲": _("Saint Pierre and Miquelon"),
        "🇻🇨": _("Saint Vincent and The Grenadines"),
        "🇼🇸": _("Samoa"),
        "🇸🇲": _("San Marino"),
        "🇸🇹": _("Sao Tome and Principe"),
        "🇸🇦": _("Saudi Arabia"),
        "🇸🇳": _("Senegal"),
        "🇷🇸": _("Serbia"),
        "🇸🇨": _("Seychelles"),
        "🇸🇱": _("Sierra Leone"),
        "🇸🇬": _("Singapore"),
        "🇸🇽": _("Sint Maarten (Dutch Part)"),
        "🇸🇰": _("Slovakia"),
        "🇸🇮": _("Slovenia"),
        "🇸🇧": _("Solomon Islands"),
        "🇸🇴": _("Somalia"),
        "🇿🇦": _("South Africa"),
        "🇬🇸": _("South Georgia"),
        "🇰🇷": _("South Korea"),
        "🇸🇸": _("South Sudan"),
        "🇪🇸": _("Spain"),
        "🇱🇰": _("Sri Lanka"),
        "🇸🇩": _("Sudan"),
        "🇸🇷": _("Suriname"),
        "🇸🇯": _("Svalbard and Jan Mayen"),
        "🇸🇿": _("Swaziland"),
        "🇸🇪": _("Sweden"),
        "🇨🇭": _("Switzerland"),
        "🇸🇾": _("Syrian Arab Republic"),
        "🇹🇼": _("Taiwan"),
        "🇹🇯": _("Tajikistan"),
        "🇹🇿": _("Tanzania"),
        "🇹🇭": _("Thailand"),
        "🇹🇱": _("Timor-Leste"),
        "🇹🇬": _("Togo"),
        "🇹🇰": _("Tokelau"),
        "🇹🇴": _("Tonga"),
        "🇹🇹": _("Trinidad and Tobago"),
        "🇹🇳": _("Tunisia"),
        "🇹🇷": _("Turkey"),
        "🇹🇲": _("Turkmenistan"),
        "🇹🇨": _("Turks and Caicos Islands"),
        "🇹🇻": _("Tuvalu"),
        "🇺🇬": _("Uganda"),
        "🇺🇦": _("Ukraine"),
        "🇦🇪": _("United Arab Emirates"),
        "🇬🇧": _("United Kingdom"),
        "🇺🇸": _("United States"),
        "🇺🇲": _("United States Minor Outlying Islands"),
        "🇺🇾": _("Uruguay"),
        "🇺🇿": _("Uzbekistan"),
        "🇻🇺": _("Vanuatu"),
        "🇻🇦": _("Vatican City"),
        "🇻🇪": _("Venezuela"),
        "🇻🇳": _("Vietnam"),
        "🇻🇬": _("Virgin Islands, British"),
        "🇻🇮": _("Virgin Islands, U.S."),
        "🇼🇫": _("Wallis and Futuna"),
        "🇪🇭": _("Western Sahara"),
        "🇾🇪": _("Yemen"),
        "🇿🇲": _("Zambia"),
        "🇿🇼": _("Zimbabwe"),
        "🇦🇽": _("Åland Islands"),
    }
    if flag_emoji:
        return f"{flag_emoji} {country_region_dict.get(flag_emoji, _('Unknown'))}"
    else:
        country_region_list = [
            f"{flag} {name}" for flag, name in country_region_dict.items()
        ]
        return country_region_list