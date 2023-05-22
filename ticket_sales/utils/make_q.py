from django.db.models import Q


def make_q_object(data):
    try:
        q_object = Q()
        for key, value in data.items():
            if isinstance(value, list):
                q_object.add(Q(**{key + "__in": value}), Q.AND)
            else:
                q_object.add(Q(**{key: value}), Q.AND)
        return q_object
    except Exception as e:
        print(e)
        return None
