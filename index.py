def update_profile(user_id, **kwargs):
    return {
        'id': user_id,
        'updated_fields': kwargs
    }



def get_domains(emails):
    for email in emails:
        if '@' in email:
            yield email.split('@')[1]



def filter_target_audience(users):
    for user in users:
        if user.get('age', 0) >= 18 and user.get('is_premium', False):
            yield user


def build_response(status_code, *errors, **payload):
    return {
        'status': status_code,
        'errors': errors,
        'data': payload
    }



def calculate_total_spent(transactions):
    return sum(transaction.get('amount', 0) for transaction in transactions)