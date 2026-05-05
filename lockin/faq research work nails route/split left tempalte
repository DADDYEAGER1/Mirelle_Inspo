import { BlogPost } from '@/types/blog';
import MDXContent from './MDXContent';
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

function renderContentWithProducts(
  html: string,
  products: BlogPost['products']
): React.ReactNode {
  if (!products || products.length === 0) {
    return <div dangerouslySetInnerHTML={{ __html: html }} />;
  }

  const parts = html.split(/({{PRODUCTS:\d+:[\d,]+}})/g);

  if (parts.length === 1) {
    return <div dangerouslySetInnerHTML={{ __html: html }} />;
  }

  return (
    <>
      {parts.map((part, index) => {
        const match = part.match(/^{{PRODUCTS:(\d+):([\d,]+)}}$/);
        if (match) {
          const count = parseInt(match[1]) as 1 | 2 | 4;
          const indices = match[2].split(',').map((i) => parseInt(i.trim()));
          if (![1, 2, 4].includes(count)) return null;
          return (
            <ProductGrid
              key={index}
              products={products}
              count={count}
              indices={indices}
            />
          );
        }
        return <div key={index} dangerouslySetInnerHTML={{ __html: part }} />;
      })}
    </>
  );
}

export default function SplitLeftTemplate({ post }: SplitLeftTemplateProps) {
  const postProducts = post.products ?? [];
console.log('postProducts in template:', JSON.stringify(postProducts));

  const mdxComponents = {
    ProductGrid: (props: any) => (
      <ProductGrid
        {...props}
        products={postProducts}
      />
    ),
  };

  const h2Blocks = post.content.split(/(?=<h2[\s>])/);
  const total = h2Blocks.length;

  const q1 = Math.max(1, Math.floor(total * 0.25));
  const q2 = Math.max(2, Math.floor(total * 0.5));
  const q3 = Math.max(3, Math.floor(total * 0.75));

  const firstSection     = h2Blocks.slice(0, q1).join('');
  const middleSection    = h2Blocks.slice(q1, q2).join('');
  const moreContent      = h2Blocks.slice(q2, q3).join('');
  const remainingContent = h2Blocks.slice(q3).join('');

  // ── MDX path ────────────────────────────────────────────────────────────────
if (post.isMDX) {
  return (
    <div className="min-h-screen bg-background">
      <div className="w-full"><InlineNewsletter /></div>

      <div className="w-full">
        <div className="hidden md:grid md:grid-cols-2 h-[600px]">
          <div className="flex items-center justify-center px-16 py-12" style={{ backgroundColor: '#f9fafb' }}>
            <div className="text-center max-w-[420px] w-full">
              {post.category && (
                <p className="font-ui text-sm uppercase tracking-wider text-gray-600 mb-4">{post.category}</p>
              )}
              <h1 className="font-heading text-[36px] md:text-[42px] leading-tight mb-4" style={{ color: '#252220' }}>
                {post.title}
              </h1>
              <p className="font-ui text-sm uppercase tracking-wide mb-2" style={{ color: '#252220' }}>BY {post.author}</p>
              <p className="font-ui text-sm text-gray-600">
                {new Date(post.date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
              </p>
            </div>
          </div>
          <div className="flex items-center justify-center p-12 overflow-hidden" style={{ backgroundColor: '#f9fafb' }}>
            {post.image && (
              <img src={post.image} alt={post.imageAlt || post.title} className="w-full h-full object-contain" />
            )}
          </div>
        </div>

        <div className="md:hidden w-full">
          <div className="text-center py-8 px-6" style={{ backgroundColor: '#f9fafb' }}>
            {post.category && (
              <p className="font-ui text-xs uppercase tracking-wider text-gray-600 mb-3">{post.category}</p>
            )}
            <h1 className="font-heading text-[36px] mb-3" style={{ color: '#252220' }}>{post.title}</h1>
            <p className="font-ui text-xs uppercase tracking-wide mb-2" style={{ color: '#252220' }}>BY {post.author}</p>
            <p className="font-ui text-xs text-gray-600">
              {new Date(post.date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
            </p>
          </div>
          {post.image && (
            <img src={post.image} alt={post.imageAlt || post.title} className="w-full h-auto" />
          )}
        </div>
      </div>

      <div className="w-full flex flex-col items-start">
        <div className="w-full max-w-[700px] px-6 md:px-12 lg:px-16 mt-12">
          <div className="mb-8">
            <Breadcrumbs
              items={[{ label: 'Blog', href: '/blog' }]}
              currentPage={post.title}
              includeSchema={false}
            />
          </div>
          <article className="prose-content-magazine">
            <MDXContent source={post.content} products={postProducts} />
          </article>
        </div>
      </div>

      <AboutEEAT />
      <FinalNewsletter />
      <ReadMoreSection currentSlug={post.slug} />
    </div>
  );
}

  // ── MD path ─────────────────────────────────────────────────────────────────
  return (
    <div className="min-h-screen bg-background">
      <div className="w-full">
        <InlineNewsletter />
      </div>

      <div className="w-full">
        <div className="hidden md:grid md:grid-cols-2 h-[600px]">
          <div className="flex items-center justify-center px-16 py-12" style={{ backgroundColor: '#f9fafb' }}>
            <div className="text-center max-w-[420px] w-full">
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
                  day: 'numeric',
                })}
              </p>
            </div>
          </div>

          <div className="flex items-center justify-center p-12 overflow-hidden" style={{ backgroundColor: '#f9fafb' }}>
            {post.image && (
              <img
                src={post.image}
                alt={post.imageAlt || post.title}
                className="w-full h-full object-contain"
              />
            )}
          </div>
        </div>

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
                day: 'numeric',
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

      <div className="w-full flex flex-col items-start">
        <div className="w-full max-w-[700px] px-6 md:px-12 lg:px-16 mt-12">
          <div className="mb-8">
            <Breadcrumbs
              items={[{ label: 'Blog', href: '/blog' }]}
              currentPage={post.title}
              includeSchema={false}
            />
          </div>

          <article className="prose-content-magazine">
            {renderContentWithProducts(firstSection, post.products)}

            {post.carouselImages && post.carouselImages.length > 0 && (
              <div className="my-12">
                <ImageCarousel images={post.carouselImages} />
              </div>
            )}

            {renderContentWithProducts(middleSection, post.products)}
            {renderContentWithProducts(moreContent, post.products)}
          </article>
        </div>

        <div className="w-full my-12">
          <InlineNewsletter />
        </div>

        <div className="w-full max-w-[700px] px-6 md:px-12 lg:px-16">
          <article className="prose-content-magazine">
            {renderContentWithProducts(remainingContent, post.products)}
          </article>
        </div>
      </div>

      <AboutEEAT />
      <FinalNewsletter />
      <ReadMoreSection currentSlug={post.slug} />
    </div>
  );
}
