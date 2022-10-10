from litreview.models import Ticket, Review, UserFollows
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from authentication.models import User
from itertools import chain
from django.db.models import CharField, Value

from . import forms, models


def posts(request):
    reviews = models.Review.objects.filter(user=request.user)
    tickets = models.Ticket.objects.filter(user=request.user)
    return render(request, 'litreview/posts.html', {'reviews': reviews,
                                                    'tickets': tickets,
                                                    'max_rating': range(5)})


@login_required
def ticket_upload(request):
    ticket_form = forms.TicketForm()

    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('posts')

    context = {
        'ticket_form': ticket_form

    }
    return render(request, 'litreview/create_ticket.html', context=context)


@login_required
def review_upload(request):
    review_form = forms.ReviewForm()
    ticket_form = forms.TicketForm()

    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if review_form.is_valid() and ticket_form.is_valid():
            review = review_form.save(commit=False)
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            review.user = request.user
            review.ticket = ticket
            ticket.save()
            review.save()

            return redirect('posts')

    context = {
        'review_form': review_form,
        'ticket_form': ticket_form

    }
    return render(request, 'litreview/create_review.html', context=context)


def review_upload_2(request, test_ticket_id):
    review_form = forms.ReviewForm()
    ticket = get_object_or_404(Ticket, id=test_ticket_id)

    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('posts')

    context = {
        'review_form': review_form,
        'ticket': ticket

    }
    return render(request, 'litreview/create_review2.html', context=context)


@login_required
def follows_searched(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')

        users = User.objects.filter(username__contains=searched)
        # print('searched', searched, 'users', users)
        return render(request, 'litreview/confirm_follow.html',
                      {'searched': searched,
                       'users': users,
                       })
    user_en_ligne = User.objects.get(id=request.user.id)
    following = user_en_ligne.following.all()
    followed = user_en_ligne.followed_by.all()
    # print('u', user_en_ligne, 'following', following, 'followed', followed)
    return render(request, 'litreview/follows.html', {'following': following,
                                                      'followed': followed,
                                                      })


@login_required
def follows(request, followed_user_id):
    if request.method == 'POST':
        # print('method post')
        follow_form = forms.FollowForm(request.POST)
        if follow_form.is_valid():
            # print('is valid')
            follow = follow_form.save(commit=False)
            follow.user = request.user
            follow.followed_user = User.objects.get(id=followed_user_id)
            follow.save()
            return redirect('follows')

    return render(request, 'litreview/follows.html')


def review_update(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    ticket = get_object_or_404(Ticket, id=review.ticket.id)
    print('review', review)
    print('ticket', ticket)
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('posts')
    else:
        review_form = forms.ReviewForm(instance=review)
    return render(request,
                  'litreview/update_review.html',
                  {'review_form': review_form,
                   'ticket': ticket})


def ticket_update(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    # print('ticket', ticket.id)
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES,
                                       instance=ticket)
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect('posts')
    else:
        ticket_form = forms.TicketForm(instance=ticket)
    return render(request,
                  'litreview/update_ticket.html',
                  {'ticket_form': ticket_form})


@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        ticket.delete()
        return redirect('posts')

    return render(request, 'litreview/delete_ticket.html', {'ticket': ticket})


@login_required
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect('posts')

    return render(request, 'litreview/delete_review.html', {'review': review})


@login_required
def follow_delete(request, follow_id):
    follow = get_object_or_404(UserFollows, id=follow_id)

    if request.method == 'POST':
        follow.delete()
        return redirect('follows')

    return render(request, 'litreview/delete_follow.html', {'follow': follow})


def get_users_viewable_reviews1(user_id):
    reviews1 = models.Review.objects.filter(user=user_id)
    print("reviews du user", reviews1)
    return reviews1


def get_users_viewable_reviews2(user_id):
    following = User.objects.get(id=user_id.id).following.all()
    print("following", following)
    followed_users = []
    for i in following:
        followed_users.append(i.followed_user)
    print("followed_users", followed_users)
    reviews2 = Review.objects.filter(user__in=followed_users)
    print("reviews des follows", reviews2)
    return reviews2


def get_users_viewable_reviews3(user_id):
    # REVIEWS POUR LES TICKETS DU USER MEME SI USER NE LES SUIT PAS
    tickets = models.Ticket.objects.filter(user=user_id)
    print("tickets du user3", tickets)
    reviews3 = Review.objects.filter(ticket__in=tickets)
    print("reviews aux tickets du user", reviews3)
    return reviews3


def get_users_viewable_tickets1(user_id):
    # TICKETS DU USER
    tickets1 = models.Ticket.objects.filter(user=user_id)
    print("tickets du user", tickets1)
    return tickets1


def get_users_viewable_tickets2(user_id):
    # TICKETS DES USERS QU'IL FOLLOW
    following = User.objects.get(id=user_id.id).following.all()
    followed_users = []
    for i in following:
        followed_users.append(i.followed_user)
    tickets2 = Ticket.objects.filter(user__in=followed_users)
    print("tickets du follow", tickets2)
    return tickets2


def feed(request):
    reviews1 = get_users_viewable_reviews1(request.user)
    reviews2 = get_users_viewable_reviews2(request.user)
    reviews3 = get_users_viewable_reviews3(request.user)
    # returns queryset of reviews
    reviews1 = reviews1.annotate(content_type=Value('REVIEW', CharField()))
    reviews2 = reviews2.annotate(content_type=Value('REVIEW', CharField()))
    reviews3 = reviews3.annotate(content_type=Value('REVIEW', CharField()))

    tickets1 = get_users_viewable_tickets1(request.user)
    tickets2 = get_users_viewable_tickets2(request.user)
    # returns queryset of tickets
    tickets1 = tickets1.annotate(content_type=Value('TICKET', CharField()))
    tickets2 = tickets2.annotate(content_type=Value('TICKET', CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews1, reviews2, reviews3, tickets1, tickets2),
        key=lambda post: post.time_created,
        reverse=True
    )
    # print('posts', posts)
    return render(request, 'litreview/feed.html',
                  context={'posts': posts, 'max_rating': range(5)})
