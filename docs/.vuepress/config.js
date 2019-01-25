const listDir = require('./utils').listDir;

const title = 'Boca';
const description = 'Tasty development tooling for Bocadillo';

module.exports = {
    base: '/boca/',
    title,
    description,
    lastUpdated: true,
    head: [
        // Twitter card meta tags
        ['meta', { name: 'twitter:card', content: 'summary' }],
        ['meta', {
            name: 'twitter:url',
            content: 'https://bocadillo.github.io/boca'
        }],
        ['meta', { name: 'twitter:site', content: title }],
        ['meta', { name: 'twitter:creator', content: 'Florimond Manca' }],
        ['meta', { name: 'twitter:title', content: title }],
        ['meta', { name: 'twitter:description', content: description }],
        ['meta', {
            name: 'twitter:image',
            content: 'https://bocadilloproject.github.io/social-image.png'
        }],
    ],
    serviceWorker: true,
    themeConfig: {
        repo: 'bocadilloproject/boca',
        docsDir: 'docs',
        docsBranch: 'release/docs',
        editLinks: true,
        editLinkText: 'Edit this page on GitHub',
        sidebarDepth: 2,
        lastUpdated: true,
        serviceWorker: { updatePopup: true },
        nav: [
            {
                text: 'Guide',
                link: '/guide/',
            },
            {
                text: 'Reference',
                link: '/reference/',
            },
            {
                text: 'Changelog',
                link: 'https://github.com/bocadilloproject/boca/blob/master/CHANGELOG.md',
            },
            {
                text: 'PyPI',
                link: 'https://pypi.org/project/boca/',
            },
        ],
        sidebar: {
            '/guide/': [
                {
                    title: 'Getting started',
                    collapsable: false,
                    children: [
                        ['/guide/', 'Introduction'],
                        '/guide/installation',
                        '/guide/basics',
                    ],
                },
                {
                    title: 'Techniques',
                    collapsable: false,
                    children: [
                        '/guide/custom-commands',
                        '/guide/programmatic-usage',
                    ]
                },
            ],
            '/reference/': [
                '/reference/',
            ]
        },
    },
};
