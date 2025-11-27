/** @type {import('next-sitemap').IConfig} */
module.exports = {
  siteUrl: 'https://mirelleinspo.com',
  generateRobotsTxt: true,
  sitemapSize: 5000,
  changefreq: 'daily',
  priority: 0.7,
  
  // ✅ Exclude non-public pages and product pages (they have their own sitemaps)
  exclude: [
    '/api/*',
    '/admin/*',
    '/server-sitemap.xml',
    '/_next/*',
    '/static/*',
    '/404',
    '/500',
    '/shop/*/[productId]', // Exclude product detail pages from main sitemap
    '/shop/christmas/*',
    '/shop/fall/*',
    '/shop/halloween/*',
    '/shop/new-year/*',
    '/shop/trendy/*',
    '/shop/winter/*',
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
  
  // ✅ Transform for existing pages (static pages only)
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
      changefreq = 'monthly';
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
  
  // ✅ Additional paths for blog posts only (main sitemap-0)
  additionalPaths: async (config) => {
    const result = [];
    
    try {
      const fs = require('fs');
      const pathModule = require('path');
      
      // Blog posts
      const blogDir = pathModule.join(process.cwd(), 'src/content/blogs');
      const dateModifiedPath = pathModule.join(process.cwd(), 'src/content/metadata/dateModified.json');
      
      if (fs.existsSync(blogDir)) {
        const files = fs.readdirSync(blogDir).filter(f => f.endsWith('.md'));
        let dateModified = {};
        
        if (fs.existsSync(dateModifiedPath)) {
          dateModified = JSON.parse(fs.readFileSync(dateModifiedPath, 'utf8'));
        }
        
        files.forEach(file => {
          const slug = file.replace('.md', '');
          const lastmod = dateModified[slug]
            ? new Date(dateModified[slug]).toISOString()
            : new Date().toISOString();
          
          result.push({
            loc: `/blog/${slug}`,
            changefreq: 'weekly',
            priority: 0.8,
            lastmod,
          });
        });
      }
      
    } catch (error) {
      console.warn('Error generating blog posts:', error.message);
    }
    
    return result;
  },
  
  // ✅ Generate separate sitemaps after build
  additionalSitemaps: [
    'https://mirelleinspo.com/sitemap-blog.xml',
    'https://mirelleinspo.com/sitemap-topics.xml',
    'https://mirelleinspo.com/sitemap-shop.xml',
    'https://mirelleinspo.com/sitemap-shop-products-index.xml',
    'https://mirelleinspo.com/sitemap-inspo.xml',
    'https://mirelleinspo.com/sitemap-images-index.xml',
  ],
};
