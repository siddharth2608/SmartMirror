class Config:

    MAGIC_MIRROR_URI = 'http://127.0.0.1:8080'
    INCLUDED_STOCKS = [{'name': 'Sensex', 'symbol': '%5EBSESN'}, {'name': 'Yes Bank', 'symbol': 'YESBANK.NS'}]
    PORTFOLIO_DETAILS = [
        {
            'fund_name': 'HDFC Gold',
            'amount_invested': 78002,
            'units_owned': 4686.206,
            'api': 'https://api.mfapi.in/mf/119132'
        },
        {
            'fund_name': 'PGIM Equity',
            'amount_invested': 14499,
            'units_owned': 424.627,
            'api': 'https://api.mfapi.in/mf/138528'
        },
        {
            'fund_name': 'Nippon Pharma',
            'amount_invested': 56497,
            'units_owned': 203.223,
            'api': 'https://api.mfapi.in/mf/118759'
        },
        {
            'fund_name': 'Kotak Multicap',
            'amount_invested': 10864,
            'units_owned': 233.921,
            'api': 'https://api.mfapi.in/mf/120166'
        },
        {
            'fund_name': 'SBI Equity Hybrid - Growth',
            'amount_invested': 25499,
            'units_owned': 128.797,
            'api': 'https://api.mfapi.in/mf/119609'
        },
        {
            'fund_name': 'ICICI Technology - Growth',
            'amount_invested': 49497,
            'units_owned': 358.668,
            'api': 'https://api.mfapi.in/mf/120594'
        }
    ]

