/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: 'https://mirelleinspo.com',
  generateRobotsTxt: true,
  sitemapSize: 5000,
  changefreq: 'daily',
  priority: 0.7,
  
  // ✅ Exclude non-public pages and dynamic content (they have their own sitemaps)
  exclude: [
    '/api/*',
    '/admin/*',
    '/server-sitemap.xml',
    '/_next/*',
    '/static/*',
    '/404',
    '/500',
    '/blog/*',              // ⭐ Exclude all blog posts - they have their own sitemap
    '/shop/*/[productId]',  // Exclude product detail pages
    '/shop/christmas/*',
    '/shop/fall/*',
    '/shop/halloween/*',
    '/shop/new-year/*',
    '/shop/trendy/*',
    '/shop/winter/*',
    '/topics/*',            // ⭐ Exclude topic pages - they have their own sitemap
    '/inspo/*',             // ⭐ Exclude inspo pages - they have their own sitemap
  ],
  
  // ✅ Enhanced robots.txt
  robotsTxtOptions: {
    policies: [
      {
        userAgent: '*',
        allow: '/',
        disallow: ['/api/', '/admin/', '/_next/', '/static/'],
      },
      // AI + crawler specific rules
      { userAgent: 'GPTBot', allow: '/', crawlDelay: 1 },
      { userAgent: 'ChatGPT-User', allow: '/' },
      { userAgent: 'Claude-Web', allow: '/', crawlDelay: 1 },
      { userAgent: 'ClaudeBot', allow: '/', crawlDelay: 1 },
      { userAgent: 'anthropic-ai', allow: '/' },
      { userAgent: 'Googlebot', allow: '/' },
      { userAgent: 'Bingbot', allow: '/' },
      { userAgent: 'CCBot', allow: '/', crawlDelay: 2 },
      { userAgent: 'PerplexityBot', allow: '/', crawlDelay: 1 },
      { userAgent: 'YouBot', allow: '/' },
      { userAgent: 'Pinterestbot', allow: '/' },
      { userAgent: 'facebookexternalhit', allow: '/' },
      { userAgent: 'PetalBot', allow: '/', crawlDelay: 2 },
      { userAgent: 'DuckDuckBot', allow: '/' },
      { userAgent: 'Slurp', allow: '/' },
      { userAgent: 'Baiduspider', allow: '/', crawlDelay: 2 },
      // Block unwanted scrapers
      { userAgent: 'SemrushBot', disallow: '/' },
      { userAgent: 'AhrefsBot', disallow: '/' },
      { userAgent: 'MJ12bot', disallow: '/' },
      { userAgent: 'DotBot', disallow: '/' },
    ],
    additionalSitemaps: [
      'https://mirelleinspo.com/sitemap-blog.xml',
      'https://mirelleinspo.com/sitemap-topics.xml',
      'https://mirelleinspo.com/sitemap-shop.xml',
      'https://mirelleinspo.com/sitemap-shop-products-index.xml',
      'https://mirelleinspo.com/sitemap-inspo.xml',
      'https://mirelleinspo.com/sitemap-images-index.xml',
    ],
  },
  
  // ✅ Transform for static pages only
  transform: async (config, path) => {
    let priority = config.priority;
    let changefreq = config.changefreq;
    let lastmod = config.autoLastmod ? new Date().toISOString() : undefined;
    
    if (path === '/') {
      priority = 1.0;
      changefreq = 'daily';
    } else if (path === '/blog') {
      priority = 0.9;
      changefreq = 'daily';
    } else if (path === '/shop') {
      priority = 0.9;
      changefreq = 'daily';
    } else if (path === '/inspo') {
      priority = 0.9;
      changefreq = 'daily';
    } else if (path === '/topics') {
      priority = 0.8;
      changefreq = 'weekly';
    } else if (['/about', '/contact', '/brands', '/pinterest', '/work-with-us'].includes(path)) {
      priority = 0.7;
      changefreq: 'monthly';
    } else if (['/privacy-policy', '/terms', '/subscribe'].includes(path)) {
      priority = 0.5;
      changefreq = 'yearly';
    }
    
    return {
      loc: path,
      changefreq,
      priority,
      lastmod,
      alternateRefs: config.alternateRefs ?? [],
    };
  },
  
  // ⭐ REMOVED additionalPaths - Blog posts are now in their own sitemap
  // This ensures sitemap-0.xml only contains static pages
};
