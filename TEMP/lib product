// src/lib/shopProducts.ts - Product Page Utilities

import type { ProductPageData, Product } from '@/types/shop';
import { getCategoryData } from '@/lib/shop';

const baseUrl = 'https://mirelleinspo.com';

/**
 * Get individual product data by category and product ID
 */
export async function getProductData(
  category: string,
  productId: string
): Promise<ProductPageData | null> {
  try {
    const productsData = await import(
      `@/content/shop-products/${category}.json`
    );
    
    const product = productsData.products[productId];
    
    if (!product) return null;
    
    return product as ProductPageData;
  } catch (error) {
    console.error(`Error loading product ${productId} from ${category}:`, error);
    return null;
  }
}

/**
 * Get all product IDs for a category (for static generation)
 */
export async function getCategoryProductIds(category: string): Promise<string[]> {
  try {
    const productsData = await import(
      `@/content/shop-products/${category}.json`
    );
    
    return Object.keys(productsData.products);
  } catch (error) {
    console.error(`Error loading product IDs for ${category}:`, error);
    return [];
  }
}

/**
 * Get related products by IDs
 */
export async function getRelatedProducts(
  category: string,
  productIds: string[],
  limit: number = 5
): Promise<Product[]> {
  try {
    const productsData = await import(
      `@/content/shop-products/${category}.json`
    );
    
    const relatedProducts: Product[] = [];
    
    for (const id of productIds.slice(0, limit)) {
      const product = productsData.products[id];
      if (product) {
        relatedProducts.push(product as Product);
      }
    }
    
    return relatedProducts;
  } catch (error) {
    console.error(`Error loading related products for ${category}:`, error);
    return [];
  }
}

/**
 * Generate Product Schema for individual product pages
 */
export function generateProductSchema(
  product: ProductPageData,
  category: string
) {
  const productUrl = `${baseUrl}/shop/${category}/${product.slug}`;
  
  return {
    '@context': 'https://schema.org',
    '@type': 'Product',
    '@id': `${productUrl}#product`,
    'name': product.name,
    'description': product.fullDescription.plainText,
    'image': `${baseUrl}${product.image}`,
    'sku': product.sku || `${category}-${product.id}`,
    'brand': {
      '@type': 'Brand',
      'name': product.brand || 'Premium Nail Brand'
    },
    'offers': {
      '@type': 'Offer',
      'url': product.affiliateUrl,
      'priceCurrency': 'USD',
      'price': product.price.replace('$', ''),
      'priceValidUntil': new Date(Date.now() + 90 * 24 * 60 * 60 * 1000)
        .toISOString()
        .split('T')[0],
      'availability': product.stockStatus === 'in-stock' 
        ? 'https://schema.org/InStock'
        : product.stockStatus === 'low-stock'
        ? 'https://schema.org/LimitedAvailability'
        : 'https://schema.org/OutOfStock',
      'seller': {
        '@type': 'Organization',
        'name': 'Amazon'
      }
    },
    ...(product.rating && product.reviewCount && {
      'aggregateRating': {
        '@type': 'AggregateRating',
        'ratingValue': product.rating.toString(),
        'reviewCount': product.reviewCount.toString(),
        'bestRating': '5',
        'worstRating': '1'
      }
    })
  };
}

/**
 * Generate Breadcrumb Schema for product pages
 */
export function generateProductBreadcrumbSchema(
  product: ProductPageData,
  category: string,
  categoryName: string
) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    'itemListElement': [
      {
        '@type': 'ListItem',
        'position': 1,
        'name': 'Home',
        'item': baseUrl
      },
      {
        '@type': 'ListItem',
        'position': 2,
        'name': 'Shop',
        'item': `${baseUrl}/shop`
      },
      {
        '@type': 'ListItem',
        'position': 3,
        'name': categoryName,
        'item': `${baseUrl}/shop/${category}`
      },
      {
        '@type': 'ListItem',
        'position': 4,
        'name': product.name,
        'item': `${baseUrl}/shop/${category}/${product.slug}`
      }
    ]
  };
}

/**
 * Generate FAQ Schema for product pages
 */
export function generateProductFAQSchema(faqs: Array<{ question: string; answer: string }>) {
  if (!faqs || faqs.length === 0) return null;
  
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    'mainEntity': faqs.map(faq => ({
      '@type': 'Question',
      'name': faq.question,
      'acceptedAnswer': {
        '@type': 'Answer',
        'text': faq.answer
      }
    }))
  };
}

/**
 * Convert product name to URL-friendly slug
 */
export function generateProductSlug(productName: string): string {
  return productName
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '') // Remove special characters
    .replace(/\s+/g, '-') // Replace spaces with hyphens
    .replace(/-+/g, '-') // Replace multiple hyphens with single
    .trim();
}

/**
 * Calculate discount percentage
 */
export function calculateDiscount(originalPrice: string, currentPrice: string): number {
  const original = parseFloat(originalPrice.replace('$', ''));
  const current = parseFloat(currentPrice.replace('$', ''));
  
  if (original === 0 || current >= original) return 0;
  
  return Math.round(((original - current) / original) * 100);
}

/**
 * Get category display name
 */
export function getCategoryDisplayName(slug: string): string {
  const categoryNames: Record<string, string> = {
    'fall': 'Fall Nails',
    'christmas': 'Christmas Nails',
    'winter': 'Winter Nails',
    'halloween': 'Halloween Nails',
    'new-year': 'New Year Nails',
    'trendy': 'Trendy Nails',
  };
  
  return categoryNames[slug] || slug.charAt(0).toUpperCase() + slug.slice(1);
}

/**
 * Get all valid internal links (from your provided list)
 */
export function getValidInternalLinks() {
  return {
    blog: [
      { slug: 'christmas-nail-designs-2025', title: 'Christmas Nail Designs 2025' },
      { slug: 'goddess-nails-2025', title: 'Goddess Nails 2025' },
      { slug: 'holiday-vacation-nails-travel-guide', title: 'Holiday Vacation Nails Travel Guide' },
      { slug: 'new-year-nails-2025', title: 'New Year Nails 2025' },
      { slug: 'valentine-nails-2026', title: 'Valentine Nails 2026' },
      { slug: 'vampire-nails-2025', title: 'Vampire Nails 2025' },
      { slug: 'wedding-nail-designs', title: 'Wedding Nail Designs' },
      { slug: 'winter-nails-2025', title: 'Winter Nails 2025' },
      { slug: 'thanksgiving-nails-2025', title: 'Thanksgiving Nails 2025' },
      { slug: 'gold-silver-chrome-christmas-nails-2025', title: 'Gold Silver Chrome Christmas Nails' },
      { slug: 'short-christmas-nails-2025', title: 'Short Christmas Nails 2025' },
      { slug: 'red-green-christmas-nails-2025', title: 'Red Green Christmas Nails' },
      { slug: 'white-christmas-nails-snowflake-designs-2025', title: 'White Christmas Nails' },
      { slug: 'blooming-gel-nails', title: 'Blooming Gel Nails' }
    ],
    inspo: [
      { slug: 'snowflake-winter-nails', title: 'Snowflake Winter Nails' },
      { slug: 'velvet-cat-eye-winter-nails', title: 'Velvet Cat Eye Winter Nails' },
      { slug: 'minimalist-winter-nails', title: 'Minimalist Winter Nails' },
      { slug: 'chocolate-brown-winter-nails', title: 'Chocolate Brown Winter Nails' },
      { slug: 'chrome-metallic-winter-nails', title: 'Chrome Metallic Winter Nails' },
      { slug: 'burgundy-wine-winter-nails', title: 'Burgundy Wine Winter Nails' }
    ],
    topics: [
      { slug: 'nail-care-guide', title: 'Nail Care Guide' },
      { slug: 'skin-tones', title: 'Skin Tones' },
      { slug: 'modern-women', title: 'Modern Women' },
      { slug: 'nail-art-guides', title: 'Nail Art Guides' },
      { slug: 'seasonal-trends', title: 'Seasonal Trends' }
    ],
    shopCategories: [
      { slug: 'fall', title: 'Fall Nails' },
      { slug: 'christmas', title: 'Christmas Nails' },
      { slug: 'winter', title: 'Winter Nails' },
      { slug: 'trendy', title: 'Trendy Nails' },
      { slug: 'new-year', title: 'New Year Nails' }
    ]
  };
}
