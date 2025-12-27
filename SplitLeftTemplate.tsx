import { BlogPost } from '@/types/blog';
import Breadcrumbs from '@/components/Breadcrumbs';
import ImageCarousel from '@/components/Blog/ImageCarousel';
import ProductGrid from '@/components/Blog/ProductGrid';
import InlineNewsletter from '@/components/Blog/InlineNewsletter';
import AboutEEAT from '@/components/Blog/AboutEEAT';
import FinalNewsletter from '@/components/Blog/FinalNewsletter';
import ReadMoreSection from '@/components/Blog/ReadMoreSection';

interface SplitLeftTemplateProps {
  post: BlogPost;
}

export default function SplitLeftTemplate({ post }: SplitLeftTemplateProps) {
  const contentSections = post.content.split(/\n\n/);
  const totalSections = contentSections.length;
  
  const section1End = Math.floor(totalSections * 0.2);
  const section2End = Math.floor(totalSections * 0.4);
  const section3End = Math.floor(totalSections * 0.6);
  
  const firstSection = contentSections.slice(0, section1End).join('\n\n');
  const middleSection = contentSections.slice(section1End, section2End).join('\n\n');
  const moreContent = contentSections.slice(section2End, section3End).join('\n\n');
  const remainingContent = contentSections.slice(section3End).join('\n\n');

  return (
    <div className="min-h-screen bg-background">
      {/* Meta Section */}
      <div className="text-center pt-12 md:pt-16 px-6">
        <p className="font-ui text-sm uppercase tracking-wider text-gray-600 mb-4">
          {post.category}
        </p>
        <h1 className="font-heading text-4xl md:text-6xl mb-6 max-w-4xl mx-auto">
          {post.title}
        </h1>
        <p className="font-ui text-sm uppercase tracking-wide mb-2">
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

      {/* Hero - Split Left */}
      <div className="mt-12 md:mt-16">
        {/* Desktop: 50/50 split */}
        <div className="hidden md:grid md:grid-cols-2 h-[600px]">
          <div className="flex items-center justify-center bg-gray-50 p-12">
            <img
              src={post.image}
              alt={post.title}
              className="max-w-full max-h-full object-contain"
            />
          </div>
          <div className="bg-gray-100"></div>
        </div>

        {/* Mobile: Centered image */}
        <div className="md:hidden px-6">
          <img
            src={post.image}
            alt={post.title}
            className="w-full h-auto rounded-lg shadow-lg"
          />
        </div>
      </div>

      {/* Breadcrumbs */}
      <div className="max-w-6xl mx-auto mt-8 px-6">
        <Breadcrumbs
          items={[{ label: 'Blog', href: '/blog' }]}
          currentPage={post.title}
          includeSchema={false}
        />
      </div>

      {/* Article Content */}
      <article className="max-w-3xl mx-auto px-6 mt-12 prose-content">
        <div dangerouslySetInnerHTML={{ __html: firstSection }} />

        {post.carouselImages && post.carouselImages.length > 0 && (
          <ImageCarousel images={post.carouselImages} />
        )}

        <div dangerouslySetInnerHTML={{ __html: middleSection }} />

        {post.products && post.products.length > 0 && (
          <ProductGrid products={post.products} layout="dual" />
        )}

        <div dangerouslySetInnerHTML={{ __html: moreContent }} />

        <InlineNewsletter />

        <div dangerouslySetInnerHTML={{ __html: remainingContent }} />
      </article>

      {/* End Sections */}
      <AboutEEAT />
      <FinalNewsletter />
      <ReadMoreSection currentSlug={post.slug} />
    </div>
  );
}