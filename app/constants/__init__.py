from app.constants import response_type, determination_type

ACKNOWLEDGMENT_DAYS_DUE = 5

CATEGORIES = [
    ('', ''),
    ('Business', 'Business'),
    ('Civic Services', 'Civic Services'),
    ('Culture & Recreation', 'Culture & Recreation'),
    ('Education', 'Education'),
    ('Government Administration', 'Government Administration'),
    ('Environment', 'Environment'),
    ('Health', 'Health'),
    ('Housing & Development', 'Housing & Development'),
    ('Public Safety', 'Public Safety'),
    ('Social Services', 'Social Services'),
    ('Transportation', 'Transportation')
]

STATES = [
    ('', ''),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District Of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
]

USER_ID_DELIMITER = '|'

UPDATED_FILE_DIRNAME = 'updated'
DELETED_FILE_DIRNAME = 'deleted'

RESPONSES_INCREMENT = 20

DEFAULT_RESPONSE_TOKEN_EXPIRY_DAYS = 20

ES_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"  # strict_date_hour_minute_second

EMAIL_TEMPLATE_FOR_TYPE = {
    response_type.FILE: "email_response_file.html",
    response_type.LINK: "email_response_link.html",
    response_type.NOTE: "email_response_note.html",
    response_type.INSTRUCTIONS: "email_response_instruction.html",
    determination_type.ACKNOWLEDGMENT: "email_response_acknowledgment.html",
    determination_type.DENIAL: "email_response_denial.html",
    determination_type.EXTENSION: "email_response_extension.html",
    determination_type.CLOSING: "email_response_closing.html",
    determination_type.EXTENSION: "email_response_extension.html",
    determination_type.REOPENED: "email_response_reopen.html"
}
