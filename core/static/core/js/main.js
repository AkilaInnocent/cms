document.addEventListener('DOMContentLoaded', () => {
    const nav = document.querySelector('.site-navbar');
    const updateNav = () => {
        if (!nav) return;
        nav.classList.toggle('scrolled', window.scrollY > 24);
    };
    updateNav();
    document.addEventListener('scroll', updateNav);

    document.querySelectorAll('.js-scroll').forEach((link) => {
        link.addEventListener('click', (event) => {
            const href = link.getAttribute('href');
            if (!href || !href.startsWith('#')) return;
            const target = document.querySelector(href);
            if (!target) return;
            event.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            document.querySelector('.navbar-collapse.show')?.classList.remove('show');
        });
    });

    const featuredVideoFrame = document.getElementById('featuredVideoFrame');
    document.querySelectorAll('.video-thumb').forEach((button) => {
        button.addEventListener('click', () => {
            if (!featuredVideoFrame) return;
            featuredVideoFrame.src = button.dataset.videoUrl;
            featuredVideoFrame.title = button.dataset.videoTitle || 'Project video';
        });
    });

    document.querySelectorAll('.project-filter').forEach((button) => {
        button.addEventListener('click', () => {
            const filter = button.dataset.filter;
            document.querySelectorAll('.project-filter').forEach((item) => item.classList.remove('active', 'btn-dark'));
            document.querySelectorAll('.project-filter').forEach((item) => item.classList.add('btn-outline-dark'));
            button.classList.add('active', 'btn-dark');
            button.classList.remove('btn-outline-dark');

            document.querySelectorAll('.project-item').forEach((item) => {
                const isVisible = filter === 'all' || item.dataset.category === filter;
                item.classList.toggle('d-none', !isVisible);
            });
        });
    });

    const modal = document.getElementById('projectPreviewModal');
    if (modal) {
        const image = modal.querySelector('#projectPreviewImage');
        const video = modal.querySelector('#projectPreviewVideo');
        const title = modal.querySelector('#projectPreviewTitle');
        const category = modal.querySelector('#projectPreviewCategory');
        const description = modal.querySelector('#projectPreviewDescription');

        document.querySelectorAll('.project-preview-trigger').forEach((trigger) => {
            trigger.addEventListener('click', () => {
                title.textContent = trigger.dataset.title || 'Project preview';
                category.textContent = trigger.dataset.category || '';
                description.textContent = trigger.dataset.description || '';

                const imageSrc = trigger.dataset.image;
                const videoSrc = trigger.dataset.video;

                if (videoSrc) {
                    video.src = videoSrc;
                    video.classList.remove('d-none');
                    image.classList.add('d-none');
                } else {
                    image.src = imageSrc;
                    image.classList.remove('d-none');
                    video.classList.add('d-none');
                    video.src = '';
                }
            });
        });

        modal.addEventListener('hidden.bs.modal', () => {
            video.src = '';
        });
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
            }
        });
    }, { threshold: 0.15 });

    document.querySelectorAll('.service-card, .project-card, .mini-stat, .contact-card').forEach((element) => {
        element.classList.add('fade-in-up');
        observer.observe(element);
    });
});
