from typing import Any
from bharu.models import Post
from bharu.models import category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = "this commands inserts post data"

    def handle(self, *args: Any, **options: Any):   
        title = [
        "Exploring how artificial intelligence is transforming industries and shaping the future today",
        "Ten practical tips for maintaining a healthy lifestyle, including habits for mind and body",
        "A beginner’s guide to learning Python efficiently and applying it in real-world projects",
        "Understanding the importance of mental health and how to improve emotional well-being",
        "Step-by-step guidance on starting a blog and growing an audience with effective strategies",
        "The rise of remote work and its impact on productivity, collaboration, and daily routines",
        "Practical eco-friendly living tips to reduce waste, save energy, and protect the planet",
        "Top productivity apps that help organize tasks, manage time, and boost efficiency daily",
        "An introduction to web development for beginners with tips on creating interactive sites",
        "Daily meditation benefits including stress reduction, focus, clarity, and emotional health",
        "Understanding blockchain technology and how it ensures secure and transparent solutions",
        "The future of electric vehicles and innovations shaping sustainable transportation globally",
        "Effective time management strategies for professionals to prioritize tasks and avoid burnout",
        "Exploring AI tools that enhance work productivity, automate tasks, and save valuable time",
        "Digital marketing strategies in 2025 for engaging audiences and improving business results",
        "A practical guide to freelancing successfully with tips on building portfolio and clients",
        "Photography tips for beginners covering lighting, composition, angles, and visual appeal",
        "Healthy eating on a budget with meal planning, smart shopping, and easy nutritious meals",
        "How to launch a YouTube channel effectively with content planning, engagement, and growth",
        "Virtual reality technology transforming entertainment, education, and professional experiences"
    ]

        content = [
        "Artificial intelligence is reshaping industries, enhancing creativity, and improving workflows across multiple sectors worldwide.",
        "Healthy lifestyle habits include exercise, proper nutrition, mindfulness, and consistent routines for physical and mental well-being.",
        "Python is ideal for beginners, offering easy syntax, powerful libraries, and opportunities for automation, web development, and data projects.",
        "Mental health awareness is key to wellness, involving stress management, emotional resilience, self-care, and mindfulness practices.",
        "Starting a blog involves choosing a niche, creating valuable content, engaging readers, and using tools to grow and monetize effectively.",
        "Remote work increases flexibility but introduces challenges like collaboration, maintaining productivity, communication, and work-life balance.",
        "Eco-friendly living practices reduce waste, conserve resources, choose sustainable products, and help protect the environment for future generations.",
        "Productivity apps streamline task management, improve focus, automate work, and help individuals and teams organize time efficiently every day.",
        "Web development for beginners includes HTML, CSS, JavaScript, and frameworks, focusing on building responsive, interactive, and appealing websites.",
        "Meditation improves mental clarity, reduces stress, increases focus, and promotes emotional balance when practiced consistently every day.",
        "Blockchain technology provides secure, transparent, decentralized solutions for finance, supply chains, digital assets, and global applications.",
        "Electric vehicles are revolutionizing transportation with sustainable energy, efficiency improvements, advanced designs, and reduced environmental impact.",
        "Time management strategies help professionals prioritize tasks, stay organized, avoid distractions, and maintain a productive work-life balance.",
        "AI-powered tools improve workflow efficiency, automate repetitive tasks, enhance creativity, and save valuable time for individuals and teams.",
        "Digital marketing in 2025 focuses on personalization, data-driven strategies, engaging content, and technology to grow audiences and revenue.",
        "Freelancing successfully requires building a strong portfolio, attracting clients, managing projects, and maintaining discipline and consistent quality work.",
        "Photography beginners improve skills with lighting, composition, angles, framing, and creative techniques for visually appealing and professional results.",
        "Healthy eating on a budget is achievable with meal planning, smart shopping, nutritious recipes, portion control, and practical dietary habits.",
        "Launching a YouTube channel requires content planning, audience engagement, video production, consistency, and strategies to grow subscribers and views.",
        "Virtual reality technology creates immersive experiences, transforming entertainment, education, professional collaboration, and social interaction."
    ]

        img_url = [
    "https://picsum.photos/id/1/200/300",
    "https://picsum.photos/id/2/200/300",
    "https://picsum.photos/id/3/200/300",
    "https://picsum.photos/id/4/200/300",
    "https://picsum.photos/id/5/200/300",
    "https://picsum.photos/id/6/200/300",
    "https://picsum.photos/id/7/200/300",
    "https://picsum.photos/id/8/200/300",
    "https://picsum.photos/id/9/200/300",
    "https://picsum.photos/id/10/200/300",
    "https://picsum.photos/id/11/200/300",
    "https://picsum.photos/id/12/200/300",
    "https://picsum.photos/id/13/200/300",
    "https://picsum.photos/id/14/200/300",
    "https://picsum.photos/id/15/200/300",
    "https://picsum.photos/id/16/200/300",
    "https://picsum.photos/id/17/200/300",
    "https://picsum.photos/id/18/200/300",
    "https://picsum.photos/id/19/200/300",
    "https://picsum.photos/id/20/200/300"
]

        categories= category.objects.all()
        for title, content, img_url in zip(title,content,img_url):
            Category = random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=Category)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))    