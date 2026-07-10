import { Toaster } from "@/components/ui/toaster"
import { QueryClientProvider } from '@tanstack/react-query'
import { queryClientInstance } from '@/lib/query-client'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PageNotFound from './lib/PageNotFound';
import { AuthProvider, useAuth } from '@/lib/AuthContext';
import { LanguageProvider } from '@/lib/LanguageContext';
import UserNotRegisteredError from '@/components/UserNotRegisteredError';
import AppLayout from './components/layout/AppLayout';
import Home from './pages/Home';
import Perfumes from './pages/Perfumes';
import Explore from './pages/Explore';
import AddPerfume from './pages/AddPerfume';
import Lists from './pages/Lists';
import Brands from './pages/Brands';
import PerfumeDetail from './pages/PerfumeDetail';
import ExportCard from './pages/ExportCard';

import WearHistory from './pages/WearHistory';
import Goals from './pages/Goals';
import Layering from './pages/Layering';
import Blog from './pages/Blog';
import BlogDetail from './pages/BlogDetail';
import AppInfo from './pages/AppInfo';
import Compare from './pages/Compare';
import Backup from './pages/Backup';
import Statistics from './pages/Statistics';
import CollectionView from './pages/CollectionView';
import BrandCollectionDetail from './pages/BrandCollectionDetail';
import OwnerGroupDetail from './pages/OwnerGroupDetail';
import Samples from './pages/Samples';
import Quotes from './pages/Quotes';
import BrandDetail from './pages/BrandDetail';
import Perfumers from './pages/Perfumers';
import PerfumersIndex from './pages/PerfumersIndex';
import PerfumerDetail from './pages/PerfumerDetail';
import Notes from './pages/Notes';
import NotesIndex from './pages/NotesIndex';
import NoteDetail from './pages/NoteDetail';
import MakePerfumePage from './pages/MakePerfume';
import TopRated from './pages/TopRated';
import PerfumeCulture from './pages/PerfumeCulture';
import Glossary from './pages/Glossary';
import GlossaryTermDetail from './pages/GlossaryTermDetail';
import Budget from './pages/Budget';
import MonthlyAnalysis from './pages/MonthlyAnalysis';
import CollectionSearch from './pages/CollectionSearch';
import StoreDetail from './pages/StoreDetail';
import AddEditBudgetEntries from './pages/AddEditBudgetEntries';
import Maestro from './pages/Maestro';
import DBViewer from './pages/DBViewer';
import MaestroBrands from './pages/maestro/MaestroBrands';
import MaestroPerfumes from './pages/maestro/MaestroPerfumes';
import MaestroNotes from './pages/maestro/MaestroNotes';
import MaestroPerfumers from './pages/maestro/MaestroPerfumers';
import MaestroQuotes from './pages/maestro/MaestroQuotes';
import MaestroGlossary from './pages/maestro/MaestroGlossary';
import MaestroStores from './pages/maestro/MaestroStores';
import MaestroCategories from './pages/maestro/MaestroCategories';
import MaestroBulkAddBrands from './pages/maestro/MaestroBulkAddBrands';
import MaestroBulkAddPerfumes from './pages/maestro/MaestroBulkAddPerfumes';
import MaestroBulkAddNotes from './pages/maestro/MaestroBulkAddNotes';
import MaestroBulkAddPerfumers from './pages/maestro/MaestroBulkAddPerfumers';
import MaestroBulkAddQuotes from './pages/maestro/MaestroBulkAddQuotes';
import MaestroBulkAddGlossary from './pages/maestro/MaestroBulkAddGlossary';
import MaestroBulkAddStores from './pages/maestro/MaestroBulkAddStores';
import MaestroOdorFamilies from './pages/maestro/MaestroOdorFamilies';
import MaestroEnums from './pages/maestro/MaestroEnums';
import MaestroTimeline from './pages/maestro/MaestroTimeline';
import MaestroWisdom from './pages/maestro/MaestroWisdom';
import MaestroAppFeatures from './pages/maestro/MaestroAppFeatures';
import Shopping from './pages/Shopping';
import ShopProductDetail from './pages/ShopProductDetail';
import IncompleteWisdom from './pages/IncompleteWisdom';
import ShopCategoryDetail from './pages/ShopCategoryDetail';
import HeadacheSensitivity from './pages/HeadacheSensitivity';
import SinusSensitivity from './pages/SinusSensitivity';
import Wishlist from './pages/Wishlist';
import MyPerfumes from './pages/MyPerfumes';
import ProcessDashboard from './pages/ProcessDashboard';
import ProcessDetail from './pages/ProcessDetail';
import AddProcess from './pages/AddProcess';
import ProcessBackup from './pages/ProcessBackup';


const AuthenticatedApp = () => {
  const { isLoadingAuth, isLoadingPublicSettings, authError, navigateToLogin } = useAuth();

  // Show loading spinner while checking app public settings or auth
  if (isLoadingPublicSettings || isLoadingAuth) {
    return (
      <div className="fixed inset-0 flex items-center justify-center">
        <div className="w-8 h-8 border-4 border-slate-200 border-t-slate-800 rounded-full animate-spin"></div>
      </div>
    );
  }

  // Handle authentication errors
  if (authError) {
    if (authError.type === 'user_not_registered') {
      return <UserNotRegisteredError />;
    } else if (authError.type === 'auth_required') {
      // Redirect to login automatically
      navigateToLogin();
      return null;
    }
  }

  // Render the main app
  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route path="/" element={<Perfumes />} />
        <Route path="/home" element={<Home />} />
        <Route path="/perfumes" element={<Perfumes />} />
        <Route path="/explore" element={<Explore />} />
        <Route path="/progress" element={<WearHistory />} />
        <Route path="/add" element={<AddPerfume />} />
        <Route path="/lists" element={<Lists />} />
        <Route path="/brands" element={<Brands />} />
        <Route path="/perfume" element={<PerfumeDetail />} />
        <Route path="/export-card" element={<ExportCard />} />
        <Route path="/wear" element={<WearHistory />} />
        <Route path="/progress" element={<WearHistory />} />
        <Route path="/goals" element={<Goals />} />
        <Route path="/layering" element={<Layering />} />
        <Route path="/blog" element={<Blog />} />
        <Route path="/blog-detail" element={<BlogDetail />} />
        <Route path="/app-info" element={<AppInfo />} />
        <Route path="/backup" element={<Backup />} />
        <Route path="/statistics" element={<Statistics />} />
        <Route path="/compare" element={<Compare />} />
        <Route path="/collection-view" element={<CollectionView />} />
        <Route path="/brand-collection" element={<BrandCollectionDetail />} />
        <Route path="/owner-group" element={<OwnerGroupDetail />} />
        <Route path="/samples" element={<Samples />} />
        <Route path="/quotes" element={<Quotes />} />
        <Route path="/brand" element={<BrandDetail />} />
        <Route path="/perfumers" element={<Perfumers />} />
        <Route path="/perfumers-index" element={<PerfumersIndex />} />
        <Route path="/perfumer" element={<PerfumerDetail />} />
        <Route path="/notes" element={<Notes />} />
        <Route path="/notes-index" element={<NotesIndex />} />
        <Route path="/note" element={<NoteDetail />} />
        <Route path="/make-perfume" element={<MakePerfumePage />} />
        <Route path="/top-rated" element={<TopRated />} />
        <Route path="/perfume-culture" element={<PerfumeCulture />} />
        <Route path="/glossary" element={<Glossary />} />
        <Route path="/glossary-term" element={<GlossaryTermDetail />} />
        <Route path="/budget" element={<Budget />} />
        <Route path="/monthly-analysis" element={<MonthlyAnalysis />} />
        <Route path="/store" element={<StoreDetail />} />
        <Route path="/collection-search" element={<CollectionSearch />} />
        <Route path="/budget-entries" element={<AddEditBudgetEntries />} />
        <Route path="/maestro" element={<Maestro />} />
        <Route path="/maestro/db-viewer" element={<DBViewer />} />
        <Route path="/admin/db-viewer" element={<DBViewer />} />
        <Route path="/maestro/brands" element={<MaestroBrands />} />
        <Route path="/maestro/perfumes" element={<MaestroPerfumes />} />
        <Route path="/maestro/notes" element={<MaestroNotes />} />
        <Route path="/maestro/perfumers" element={<MaestroPerfumers />} />
        <Route path="/maestro/quotes" element={<MaestroQuotes />} />
        <Route path="/maestro/glossary" element={<MaestroGlossary />} />
        <Route path="/maestro/perfume-stores" element={<MaestroStores />} />
        <Route path="/maestro/categories" element={<MaestroCategories />} />
        <Route path="/maestro/brands/bulk-add" element={<MaestroBulkAddBrands />} />
        <Route path="/maestro/perfumes/bulk-add" element={<MaestroBulkAddPerfumes />} />
        <Route path="/maestro/notes/bulk-add" element={<MaestroBulkAddNotes />} />
        <Route path="/maestro/perfumers/bulk-add" element={<MaestroBulkAddPerfumers />} />
        <Route path="/maestro/quotes/bulk-add" element={<MaestroBulkAddQuotes />} />
        <Route path="/maestro/glossary/bulk-add" element={<MaestroBulkAddGlossary />} />
        <Route path="/maestro/perfume-stores/bulk-add" element={<MaestroBulkAddStores />} />
        <Route path="/maestro/odor-families" element={<MaestroOdorFamilies />} />
        <Route path="/maestro/enums" element={<MaestroEnums />} />
        <Route path="/maestro/timeline" element={<MaestroTimeline />} />
        <Route path="/maestro/wisdom" element={<MaestroWisdom />} />
        <Route path="/maestro/app-features" element={<MaestroAppFeatures />} />
        <Route path="/shopping" element={<Shopping />} />
        <Route path="/shop-product" element={<ShopProductDetail />} />
        <Route path="/shop-category/:categoryId" element={<ShopCategoryDetail />} />
        <Route path="/incomplete-wisdom" element={<IncompleteWisdom />} />
        <Route path="/headache" element={<HeadacheSensitivity />} />
        <Route path="/sinus" element={<SinusSensitivity />} />
        <Route path="/wishlist" element={<Wishlist />} />
        <Route path="/my-perfumes" element={<MyPerfumes />} />
        <Route path="/process" element={<ProcessDashboard />} />
        <Route path="/process/:id" element={<ProcessDetail />} />
        <Route path="/add-process" element={<AddProcess />} />
        <Route path="/process-backup" element={<ProcessBackup />} />
      </Route>
      <Route path="*" element={<PageNotFound />} />
    </Routes>
  );
};


function App() {

  return (
    <LanguageProvider>
      <AuthProvider>
        <QueryClientProvider client={queryClientInstance}>
          <Router>
            <AuthenticatedApp />
          </Router>
          <Toaster />
        </QueryClientProvider>
      </AuthProvider>
    </LanguageProvider>
  )
}

export default App