import { BlogPost } from '@/types/blog';
import Breadcrumbs from '@/components/Breadcrumbs';
import ImageCarousel from '@/components/Blog/ImageCarousel';
import ProductGrid from '@/components/Blog/ProductGrid';
import InlineNewsletter from '@/components/Blog/InlineNewsletter';
import AboutEEAT from '@/components/Blog/AboutEEAT';
import FinalNewsletter from '@/components/Blog/FinalNewsletter';
import ReadMoreSection from '@/components/Blog/ReadMoreSection';

import TableOfContents from '@/components/Blog/TableOfContents';  

interface SplitLeftTemplateProps {
  post: BlogPost;
}

export default function SplitLeftTemplate({ post }: SplitLeftTemplateProps) {
  const h2Blocks = post.content.split(/(?=<h2[\s>])/);
  const total = h2Blocks.length;

  const q1 = Math.max(1, Math.floor(total * 0.25));
  const q2 = Math.max(2, Math.floor(total * 0.5));
  const q3 = Math.max(3, Math.floor(total * 0.75));

  const firstSection     = h2Blocks.slice(0, q1).join('');
  const middleSection    = h2Blocks.slice(q1, q2).join('');
  const moreContent      = h2Blocks.slice(q2, q3).join('');
  const remainingContent = h2Blocks.slice(q3).join('');


  return (
    <div className="min-h-screen bg-background">
      {/* Inline Newsletter */}
      <div className="w-full">
        <InlineNewsletter />
      </div>

      {/* Hero - Split Left */}
      <div className="w-full">
        {/* Desktop: 50/50 split with brand colors */}
        <div className="hidden md:grid md:grid-cols-2 h-[600px]">
          {/* LEFT SIDE - METADATA with brand background */}
          <div className="flex items-center justify-center p-12" style={{ backgroundColor: '#f9fafb' }}>
            <div className="text-center">
              {post.category && (
                <p className="font-ui text-sm uppercase tracking-wider text-gray-600 mb-4">
                  {post.category}
                </p>
              )}
              <h1 className="font-heading text-[36px] md:text-[42px] leading-tight mb-4" style={{ color: '#252220' }}>
                {post.title}
              </h1>
              <p className="font-ui text-sm uppercase tracking-wide mb-2" style={{ color: '#252220' }}>
                BY {post.author}
              </p>
              <p className="font-ui text-sm text-gray-600">
                {new Date(post.date).toLocaleDateString('en-US', { 
                  year: 'numeric', 
                  month: 'long', 
                  day: 'numeric' 
                })}
              </p>
            </div>
          </div>

          {/* RIGHT SIDE - IMAGE with brand background */}
          <div className="flex items-center justify-center p-12" style={{ backgroundColor: '#f9fafb' }}>
            {post.image && (
              <img
                src={post.image}
                alt={post.imageAlt || post.title}
                className="max-w-full max-h-full object-contain"
              />
            )}
          </div>
        </div>

        {/* Mobile: Stacked */}
        <div className="md:hidden w-full">
          <div className="text-center py-8 px-6" style={{ backgroundColor: '#f9fafb' }}>
            {post.category && (
              <p className="font-ui text-xs uppercase tracking-wider text-gray-600 mb-3">
                {post.category}
              </p>
            )}
            <h1 className="font-heading text-[36px] mb-3" style={{ color: '#252220' }}>
              {post.title}
            </h1>
            <p className="font-ui text-xs uppercase tracking-wide mb-2" style={{ color: '#252220' }}>
              BY {post.author}
            </p>
            <p className="font-ui text-xs text-gray-600">
              {new Date(post.date).toLocaleDateString('en-US', { 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
              })}
            </p>
          </div>
          {post.image && (
            <img
              src={post.image}
              alt={post.imageAlt || post.title}
              className="w-full h-auto"
            />
          )}
        </div>
      </div>

      {/* Article Content - Vogue Style Narrow Column */}
      <div className="w-full flex flex-col items-start">
        {/* Narrow content container */}
        <div className="w-full max-w-[700px] px-6 md:px-12 lg:px-16 mt-12">
          
          {/* Breadcrumbs */}
          <div className="mb-8">
            <Breadcrumbs
              items={[{ label: 'Blog', href: '/blog' }]}
              currentPage={post.title}
              includeSchema={false}
            />
          </div>
          
          

          {/* Article Content - LEFT ALIGNED, 20px font */}
          <article className="prose-content-magazine">
            <div dangerouslySetInnerHTML={{ __html: firstSection }} />

            {post.carouselImages && post.carouselImages.length > 0 && (
              <div className="my-12">
                <ImageCarousel images={post.carouselImages} />
              </div>
            )}

            <div dangerouslySetInnerHTML={{ __html: middleSection }} />

{post.products && post.products.length > 0 && (
  <div className="my-12">
    <ProductGrid 
      products={post.products} 
      count={2}
      indices={post.products.map((_, i) => i)}
    />
  </div>
)}

            <div dangerouslySetInnerHTML={{ __html: moreContent }} />
          </article>
        </div>

        {/* Break out - Full width newsletter */}
        <div className="w-full my-12">
          <InlineNewsletter />
        </div>

        {/* Resume narrow content container */}
        <div className="w-full max-w-[700px] px-6 md:px-12 lg:px-16">
          <article className="prose-content-magazine">
            <div dangerouslySetInnerHTML={{ __html: remainingContent }} />
          </article>
        </div>
      </div>

      {/* End Sections */}
      <AboutEEAT />
      <FinalNewsletter />
      <ReadMoreSection currentSlug={post.slug} />
    </div>
  );
}
