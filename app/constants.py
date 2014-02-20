# Engagement
ENGAGEMENT_TYPES = ['External', 'Internal']
NUMBER_OF_REPORTS = 1
RETESTING_HOURS = 4
APPLIANCES = ['Firewall', 'IPS', 'IDS', 'WAF']
REPORTING_FREQUENCY = ['Daily Reporting', 'Weekly Reporting']
ENVIRONMENT = ['Engagemention', 'Development', 'Staging', 'Disaster Recovery']

# Application
SIZE_OF_APPLICATION = ['1-25', '25-50', '75-100', '100-150', '150-200',
                       '200-200', '300-500', '500+']
TWO_FACTOR_METHODS = ['RSA Token',
                      'Google Authenticator',
                      'Client Certificate',
                      'Other']

# API
DOCUMENTATION_QUALITY = ['Non-Existant',
                         'Contextual Only (no sample requests)',
                         'Sample Requests Only',
                         'Sample Requests & Data Types',
                         'Sample Requests, Data Types, and Sample Values']
MESSAGE_FORMAT = ['SOAP',
                  'JSON',
                  'XML',
                  'Binary Protocol',
                  'Standard GET/POST',
                  'Other']

# Perspective
HARDWARE = ['Netbook',
            'Thumbdrive',
            'None Needed']


##########################
# Labels
##########################
# Engagement
TYPE_LABEL = 'Type of Engagement'
RENEWAL_LABEL = 'Renewal Opportunity'
NUMBER_OF_REPORTS_LABEL = 'Number of Reports'
RETESTING_HOURS_LABEL = 'Number of Retesting Hours'

# Constraints
REPORTING_FREQUENCY_LABEL = 'Reporting Frequency'
TIME_WINDOW_LABEL = 'Testing Hours Restriction'
DEADLINE_LABEL = 'Report Deadline'
SECURITY_APPLIANCES_LABEL = 'Security Appliances'
PERMIT_WHITELISTING_LABEL = 'Customer Willing to Whitelist'
RESTRICTIONS_LABEL = 'Bandwidth Restrictions'
BANDWIDTH_RESTRICTIONS_LABEL = 'What Restrictions?'
USES_THIRD_PARTIES_LABEL = 'Third Party Hosted / Managed / Owned'
THIRD_PARTIES_LABEL = 'List Third Parties'
PAST_ISSUES_LABEL = 'Issues in Previous Years'
NOTES_LABEL = 'Internal Notes'

# Application
LINK_LABEL = 'Link'
NON_AUTH_ASSESSMENT_LABEL = 'Opt Out of Authenticated Testing'
REQUIRES_AUTH_LABEL = 'Requires Authentication'
ROLE_COUNT_LABEL = 'Number of Roles'
ROLES_LABEL = 'List Roles'
PUBLIC_REGISTRATION_LABEL = 'Registration is Publicly Available'
SIZE_LABEL = 'Number of Methods / Dynamic Pages'

# Constraints
BLACKLISTED_PAGES_LABEL = 'Blacklisted Methods / Pages'
REQUIRES_TWO_FACTOR_LABEL = 'Requires Two Factor Authentication'
TWO_FACTOR_METHODS_LABEL = 'Which Technology'
LIVE_DATABASE_LABEL = 'Live Database'

# API
DOCUMENTATION_LABEL = 'Documentation'
DOCUMENTATION_QUALITY_LABEL = 'Documentation Quality'
MESSAGE_FORMAT_LABEL = 'Application Layer Message Format'
PREPOPULATED_OBJECTS_LABEL = 'Providing Pre-Populated Objects'
TEST_SUITES_AVAILABLE_LABEL = 'Test Suites Available'

# Constraints
OS_SPECIFIC_LABEL = 'OS Specific'
REQUIRES_INSTALLATION_LABEL = 'Requires Installation'
HARDWARE_REQUIREMENT_LABEL = 'Hardware Requirement'
HMAC_REQUIRED = 'Requires HMAC'

# NetworkLayer
SCOPE_LABEL = 'Scope'
UNIQUE_SERVICES_LABEL = 'Number of Unique Services'
