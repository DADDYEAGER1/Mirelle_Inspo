const fs = require('fs');
const path = require('path');

const SITE_URL = 'https://mirelleinspo.com';
const PUBLIC_DIR = path.join(process.cwd(), 'public');

// ✅ Helper: Get current season
function getCurrentSeason() {
  const month = new Date().getMonth();
  if (month >= 2 && month <= 4) return 'spring';
  if (month >= 5 && month <= 7) return 'summer';
  if (month >= 8 && month <= 10) return 'fall';
  return 'winter';
}

// ✅ Helper: Create XML sitemap
function createSitemap(urls) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(url => `  <url>
    <loc>${url.loc}</loc>
    <lastmod>${url.lastmod || new Date().toISOString()}</lastmod>
    <changefreq>${url.changefreq || 'weekly'}</changefreq>
    <priority>${url.priority || 0.7}</priority>
  </url>`).join('\n')}
</urlset>`;
}

// ✅ Helper: Create sitemap index
function createSitemapIndex(sitemaps) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemaps.map(sitemap => `  <sitemap>
    <loc>${SITE_URL}/${sitemap}</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
  </sitemap>`).join('\n')}
</sitemapindex>`;
}

// ✅ Helper: Create image sitemap
function createImageSitemap(images) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
${images.map(img => `  <url>
    <loc>${img.pageUrl}</loc>
    <image:image>
      <image:loc>${img.imageUrl}</image:loc>
      <image:title>${img.title}</image:title>
      ${img.caption ? `<image:caption>${img.caption}</image:caption>` : ''}
    </image:image>
  </url>`).join('\n')}
</urlset>`;
}

// ========================================
// 1️⃣ GENERATE BLOG SITEMAP
// ========================================
function generateBlogSitemap() {
  console.log('📄 Generating blog sitemap...');
  
  try {
    const blogDir = path.join(process.cwd(), 'src/content/blogs');
    const dateModifiedPath = path.join(process.cwd(), 'src/content/metadata/dateModified.json');
    
    if (!fs.existsSync(blogDir)) {
      console.warn('⚠️  Blog directory not found, skipping...');
      return;
    }
    
    const files = fs.readdirSync(blogDir).filter(f => f.endsWith('.md'));
    
    if (files.length === 0) {
      console.warn('⚠️  No blog posts found');
      return;
    }
    
    // Load date modified metadata
    let dateModified = {};
    if (fs.existsSync(dateModifiedPath)) {
      dateModified = JSON.parse(fs.readFileSync(dateModifiedPath, 'utf8'));
    }
    
    // Generate URLs for all blog posts
    const urls = files.map(file => {
      const slug = file.replace('.md', '');
      const lastmod = dateModified[slug]
        ? new Date(dateModified[slug]).toISOString()
        : new Date().toISOString();
      
      return {
        loc: `${SITE_URL}/blog/${slug}`,
        changefreq: 'weekly',
        priority: 0.8,
        lastmod,
      };
    });
    
    const xml = createSitemap(urls);
    fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-blog.xml'), xml);
    console.log(`✅ sitemap-blog.xml created (${urls.length} blog posts)`);
    
  } catch (error) {
    console.error('❌ Error generating blog sitemap:', error.message);
  }
}

// ========================================
// 2️⃣ GENERATE TOPICS SITEMAP
// ========================================
function generateTopicsSitemap() {
  console.log('📄 Generating topics sitemap...');
  
  const topics = [
    { slug: 'at-home-hacks', priority: 0.7 },
    { slug: 'modern-women', priority: 0.7 },
    { slug: 'nail-care-guide', priority: 0.8 },
    { slug: 'seasonal-trends', priority: 0.8 },
    { slug: 'skin-tones', priority: 0.7 },
  ];
  
  const urls = [
    {
      loc: `${SITE_URL}/topics`,
      changefreq: 'weekly',
      priority: 0.8,
      lastmod: new Date().toISOString(),
    },
    ...topics.map(topic => ({
      loc: `${SITE_URL}/topics/${topic.slug}`,
      changefreq: 'weekly',
      priority: topic.priority,
      lastmod: new Date().toISOString(),
    }))
  ];
  
  const xml = createSitemap(urls);
  fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-topics.xml'), xml);
  console.log('✅ sitemap-topics.xml created');
}

// ========================================
// 3️⃣ GENERATE SHOP CATEGORY PAGES SITEMAP
// ========================================
function generateShopSitemap() {
  console.log('📄 Generating shop category pages sitemap...');
  
  const categories = ['christmas', 'fall', 'halloween', 'new-year', 'trendy', 'winter'];
  
  const urls = [
    {
      loc: `${SITE_URL}/shop`,
      changefreq: 'daily',
      priority: 0.9,
      lastmod: new Date().toISOString(),
    },
    ...categories.map(cat => ({
      loc: `${SITE_URL}/shop/${cat}`,
      changefreq: 'weekly',
      priority: 0.8,
      lastmod: new Date().toISOString(),
    }))
  ];
  
  const xml = createSitemap(urls);
  fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-shop.xml'), xml);
  console.log('✅ sitemap-shop.xml created');
}

// ========================================
// 4️⃣ GENERATE SHOP PRODUCTS SITEMAPS (per category)
// ========================================
function generateShopProductsSitemaps() {
  console.log('📄 Generating shop product sitemaps...');
  
  const categories = ['christmas', 'fall', 'halloween', 'new-year', 'trendy', 'winter'];
  const productSitemaps = [];
  
  categories.forEach(category => {
    try {
      const productFile = path.join(process.cwd(), `src/content/shop-products/${category}.json`);
      
      if (!fs.existsSync(productFile)) {
        console.warn(`⚠️  ${category}.json not found, skipping...`);
        return;
      }
      
      const data = JSON.parse(fs.readFileSync(productFile, 'utf8'));
      
      // Extract products from the nested structure: data.products is an object with numeric keys
      const productsObj = data.products || {};
      const products = Object.values(productsObj);
      
      if (products.length === 0) {
        console.warn(`⚠️  No products found in ${category}.json`);
        return;
      }
      
      const urls = products.map(product => ({
        loc: `${SITE_URL}/shop/${category}/${product.slug}`,
        changefreq: 'weekly',
        priority: 0.7,
        lastmod: new Date().toISOString(),
      }));
      
      const xml = createSitemap(urls);
      const filename = `sitemap-shop-products-${category}.xml`;
      fs.writeFileSync(path.join(PUBLIC_DIR, filename), xml);
      productSitemaps.push(filename);
      console.log(`✅ ${filename} created (${products.length} products)`);
      
    } catch (error) {
      console.error(`❌ Error generating ${category} products sitemap:`, error.message);
    }
  });
  
  // Create products index
  if (productSitemaps.length > 0) {
    const indexXml = createSitemapIndex(productSitemaps);
    fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-shop-products-index.xml'), indexXml);
    console.log('✅ sitemap-shop-products-index.xml created');
  }
}

// ========================================
// 5️⃣ GENERATE INSPO CATEGORY PAGES SITEMAP
// ========================================
function generateInspoSitemap() {
  console.log('📄 Generating inspo category pages sitemap...');
  
  try {
    const inspoDir = path.join(process.cwd(), 'src/content/inspo-images');
    const files = fs.readdirSync(inspoDir).filter(f => f.endsWith('.json'));
    
    const urls = [
      {
        loc: `${SITE_URL}/inspo`,
        changefreq: 'daily',
        priority: 0.9,
        lastmod: new Date().toISOString(),
      },
      ...files.map(file => ({
        loc: `${SITE_URL}/inspo/${file.replace('.json', '')}`,
        changefreq: 'weekly',
        priority: 0.8,
        lastmod: new Date().toISOString(),
      }))
    ];
    
    const xml = createSitemap(urls);
    fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-inspo.xml'), xml);
    console.log(`✅ sitemap-inspo.xml created (${files.length} categories)`);
    
  } catch (error) {
    console.error('❌ Error generating inspo sitemap:', error.message);
  }
}

// ========================================
// 6️⃣ GENERATE IMAGE SITEMAPS WITH SMART CAPTIONS
// ========================================
function generateImageSitemaps() {
  console.log('📸 Generating image sitemaps with smart captions...');
  
  const imageSitemaps = [];
  const currentYear = new Date().getFullYear();
  const season = getCurrentSeason();
  
  // 6a) Blog images (from /public/images/blog/) - FLAT STRUCTURE
  try {
    const blogImagesDir = path.join(PUBLIC_DIR, 'images', 'blog');
    
    if (fs.existsSync(blogImagesDir)) {
      const imageFiles = fs.readdirSync(blogImagesDir).filter(f => 
        /\.(jpg|jpeg|png|webp)$/i.test(f)
      );
      
      // Get all blog posts
      const blogDir = path.join(process.cwd(), 'src/content/blogs');
      const blogPosts = fs.existsSync(blogDir) 
        ? fs.readdirSync(blogDir).filter(f => f.endsWith('.md')).map(f => f.replace('.md', ''))
        : [];
      
      const blogImages = imageFiles.map(img => {
        const imageName = img.replace(/\.(jpg|jpeg|png|webp)$/i, '');
        
        // Try to match image to blog post
        const matchedPost = blogPosts.find(post => imageName.includes(post) || post.includes(imageName));
        const slug = matchedPost || imageName.replace(/-(hero|thumb|\d+)$/i, '');
        const cleanTitle = slug.replace(/-/g, ' ');
        
        // Generate unique caption based on image type
        let caption;
        if (imageName.includes('hero')) {
          caption = `Complete ${cleanTitle} tutorial with expert tips and techniques`;
        } else if (imageName.includes('step')) {
          caption = `Step-by-step process for achieving ${cleanTitle} look`;
        } else if (imageName.match(/\d+$/)) {
          caption = `${cleanTitle} design variation and styling inspiration`;
        } else {
          caption = `Professional ${cleanTitle} guide with detailed instructions`;
        }
        
        return {
          pageUrl: `${SITE_URL}/blog/${slug}`,
          imageUrl: `${SITE_URL}/images/blog/${img}`,
          title: `${cleanTitle} - ${currentYear} nail art guide`,
          caption: caption,
        };
      });
      
      const xml = createImageSitemap(blogImages);
      fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-images-blog.xml'), xml);
      imageSitemaps.push('sitemap-images-blog.xml');
      console.log(`✅ sitemap-images-blog.xml created (${blogImages.length} images with unique captions)`);
    }
  } catch (error) {
    console.error('❌ Error generating blog images sitemap:', error.message);
  }
  
  // 6b) Shop product images (from /public/images/shop/) - FLAT STRUCTURE
  try {
    const shopImagesDir = path.join(PUBLIC_DIR, 'images', 'shop');
    
    if (fs.existsSync(shopImagesDir)) {
      const imageFiles = fs.readdirSync(shopImagesDir).filter(f => 
        /\.(jpg|jpeg|png|webp)$/i.test(f)
      );
      
      // Get all products from all categories to match images
      const categories = ['christmas', 'fall', 'halloween', 'new-year', 'trendy', 'winter'];
      const allProducts = [];
      
      categories.forEach(category => {
        const productFile = path.join(process.cwd(), `src/content/shop-products/${category}.json`);
        if (fs.existsSync(productFile)) {
          const data = JSON.parse(fs.readFileSync(productFile, 'utf8'));
          const productsObj = data.products || {};
          const products = Object.values(productsObj);
          
          products.forEach(product => {
            allProducts.push({
              category,
              slug: product.slug,
              image: product.image,
              name: product.name || `${category} nail design`,
            });
          });
        }
      });
      
      const shopImages = imageFiles.map(img => {
        // Try to find matching product by image path
        const imagePath = `/images/shop/${img}`;
        const matchedProduct = allProducts.find(p => p.image === imagePath);
        
        if (matchedProduct) {
          const categoryName = matchedProduct.category.replace(/-/g, ' ');
          const caption = `${matchedProduct.name} - Professional ${categoryName} nail art design for ${season} season ${currentYear}`;
          
          return {
            pageUrl: `${SITE_URL}/shop/${matchedProduct.category}/${matchedProduct.slug}`,
            imageUrl: `${SITE_URL}/images/shop/${img}`,
            title: matchedProduct.name,
            caption: caption,
          };
        }
        
        // Fallback: use shop main page if no match
        return {
          pageUrl: `${SITE_URL}/shop`,
          imageUrl: `${SITE_URL}/images/shop/${img}`,
          title: `Premium nail design product`,
          caption: `Trending nail art design inspiration - Perfect for special occasions and events`,
        };
      });
      
      const xml = createImageSitemap(shopImages);
      fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-images-shop.xml'), xml);
      imageSitemaps.push('sitemap-images-shop.xml');
      console.log(`✅ sitemap-images-shop.xml created (${shopImages.length} images with unique captions)`);
    }
  } catch (error) {
    console.error('❌ Error generating shop images sitemap:', error.message);
  }
  
  // 6c) Inspo gallery images (from /public/inspo/)
  try {
    const inspoPublicDir = path.join(PUBLIC_DIR, 'inspo');
    
    if (fs.existsSync(inspoPublicDir)) {
      const inspoImages = [];
      const categories = fs.readdirSync(inspoPublicDir).filter(f => 
        fs.statSync(path.join(inspoPublicDir, f)).isDirectory()
      );
      
      // Descriptive variations for uniqueness
      const descriptors = [
        'trending style and modern techniques',
        'creative design ideas and inspiration',
        'elegant look with professional finish',
        'unique artistic approach and styling',
        'popular trend with expert guidance',
        'stunning visual inspiration and ideas',
        'contemporary design with detailed tutorial',
        'innovative nail art technique showcase'
      ];
      
      categories.forEach(category => {
        const categoryDir = path.join(inspoPublicDir, category);
        const imageFiles = fs.readdirSync(categoryDir).filter(f => 
          /\.(jpg|jpeg|png|webp)$/i.test(f)
        );
        
        imageFiles.forEach((img, index) => {
          const categoryName = category.replace(/-/g, ' ');
          const descriptor = descriptors[index % descriptors.length];
          const imageNumber = img.match(/\d+/)?.[0] || (index + 1);
          
          inspoImages.push({
            pageUrl: `${SITE_URL}/inspo/${category}`,
            imageUrl: `${SITE_URL}/inspo/${category}/${img}`,
            title: `${categoryName} nail inspiration ${imageNumber}`,
            caption: `${categoryName} nail art - ${descriptor}`,
          });
        });
      });
      
      const xml = createImageSitemap(inspoImages);
      fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-images-inspo.xml'), xml);
      imageSitemaps.push('sitemap-images-inspo.xml');
      console.log(`✅ sitemap-images-inspo.xml created (${inspoImages.length} images with unique captions)`);
    }
  } catch (error) {
    console.error('❌ Error generating inspo images sitemap:', error.message);
  }
  
  // 6d) Topics images (from /public/images/topics/) - FLAT STRUCTURE
  try {
    const topicsImagesDir = path.join(PUBLIC_DIR, 'images', 'topics');
    
    if (fs.existsSync(topicsImagesDir)) {
      const imageFiles = fs.readdirSync(topicsImagesDir).filter(f => 
        /\.(jpg|jpeg|png|webp)$/i.test(f) && f !== '.gitkeep'
      );
      
      const topics = [
        'at-home-hacks',
        'modern-women',
        'nail-care-guide',
        'seasonal-trends',
        'skin-tones',
      ];
      
      // Unique descriptions for each topic
      const topicCaptions = {
        'at-home-hacks': 'DIY nail care tips and tricks you can easily do at home',
        'modern-women': 'Contemporary nail styles perfect for today\'s professional woman',
        'nail-care-guide': 'Essential nail health and maintenance techniques for beautiful nails',
        'seasonal-trends': `Latest ${season} ${currentYear} nail design trends and color palettes`,
        'skin-tones': 'Perfect nail colors matched to different skin tones and undertones',
      };
      
      const topicsImages = imageFiles.map(img => {
        const imageName = img.replace(/\.(jpg|jpeg|png|webp)$/i, '');
        
        // Try to match image to topic
        const matchedTopic = topics.find(topic => imageName.includes(topic) || topic.includes(imageName));
        const slug = matchedTopic || imageName;
        const cleanTitle = slug.replace(/-/g, ' ');
        
        return {
          pageUrl: `${SITE_URL}/topics/${slug}`,
          imageUrl: `${SITE_URL}/images/topics/${img}`,
          title: `${cleanTitle} - Expert nail care guidance`,
          caption: topicCaptions[slug] || `Learn ${cleanTitle} - Expert advice and techniques for nail enthusiasts`,
        };
      });
      
      if (topicsImages.length > 0) {
        const xml = createImageSitemap(topicsImages);
        fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-images-topics.xml'), xml);
        imageSitemaps.push('sitemap-images-topics.xml');
        console.log(`✅ sitemap-images-topics.xml created (${topicsImages.length} images with unique captions)`);
      }
    }
  } catch (error) {
    console.error('❌ Error generating topics images sitemap:', error.message);
  }
  
  // Create images index
  if (imageSitemaps.length > 0) {
    const indexXml = createSitemapIndex(imageSitemaps);
    fs.writeFileSync(path.join(PUBLIC_DIR, 'sitemap-images-index.xml'), indexXml);
    console.log('✅ sitemap-images-index.xml created');
  }
}

// ========================================
// 🚀 RUN ALL GENERATORS
// ========================================
async function main() {
  console.log('🚀 Starting sitemap generation...\n');
  
  // Ensure public directory exists
  if (!fs.existsSync(PUBLIC_DIR)) {
    fs.mkdirSync(PUBLIC_DIR, { recursive: true });
  }
  
  generateBlogSitemap();
  generateTopicsSitemap();
  generateShopSitemap();
  generateShopProductsSitemaps();
  generateInspoSitemap();
  generateImageSitemaps();
  
  console.log('\n✅ All sitemaps generated successfully with smart, unique captions!');
  console.log('\n📋 Generated sitemaps:');
  console.log('   • sitemap-blog.xml (blog posts)');
  console.log('   • sitemap-topics.xml (topics pages)');
  console.log('   • sitemap-shop.xml (shop categories)');
  console.log('   • sitemap-shop-products-*.xml (products)');
  console.log('   • sitemap-inspo.xml (inspo galleries)');
  console.log('   • sitemap-images-*.xml (images with SEO-optimized captions)');
  console.log('\n📋 Next steps:');
  console.log('1. Run: npm run postbuild (to generate sitemap-0.xml for static pages)');
  console.log('2. Verify all sitemaps in /public directory');
  console.log('3. Check image sitemaps for unique, descriptive captions');
  console.log('4. Submit sitemap.xml to Google Search Console');
}

main().catch(error => {
  console.error('❌ Fatal error:', error);
  process.exit(1);
});
