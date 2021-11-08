from articleapp.models import Article
from django.http import HttpResponseForbidden

#유저가 같은지 확인하는 데코레이터
def article_ownership_required(func):
    def decorated(request,*args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)
    return decorated