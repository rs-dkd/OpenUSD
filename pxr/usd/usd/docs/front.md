# Usd : Universal Scene Description (Core) {#usd_page_front}
\if ( PIXAR_MFB_BUILD )
\mainpage Usd : Universal Scene Description
\endif

<b>Usd</b> is the core client-facing module for authoring, composing, 
and reading Universal Scene Description. USD is designed to encode scalable, 
hierarchically organized, static and time-sampled data, for the primary 
purpose of interchanging and augmenting the data between cooperating Digital 
Content Creation applications. 

## Core API Manual {#Usd_ManualDesc}

This manual contains the API documentation for the core Usd module, prefaced
with an introduction to the key concepts behind the API, and including a
guide to making effective use of the API.  In this manual we do not deeply
explore the composition semantics that underly Usd scenegraphs - that is the
domain of the (forthcoming) <em>Universal Scene Description Composition
Compendium</em>.  We will discuss some aspects of the composition operators,
primarily as they affect authoring workflows and/or scalability and/or
import/export.

<!-- This should totally be done with CSS instead of table and hokey spaces -->
\n

<table border="0">
<tr>
     <td> <b>API Manual</b> </td>    
     <td> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </td>
     <td> <b>Key Classes</b></td>
</tr>

<tr>
<td>
<ol>
<li> \subpage Usd_Page_ObjectModel </li>
     <ol type="i">
     <li> \ref Usd_OM_SdfLayer </li>
     <li> \ref Usd_OM_UsdStage </li>
     <li> \ref Usd_OM_UsdPrim </li>
     <li> \ref Usd_OM_UsdProperty </li>
     <li> \ref Usd_OM_UsdAttribute </li>
     <li> \ref Usd_OM_UsdRelationship </li>
     <li> \ref Usd_OM_Metadata </li>
     <li> \ref Usd_OM_OtherObjects </li>
     </ol>
<li> \subpage Usd_Page_Datatypes </li>
     <ol type="i">
     <li> \ref Usd_Datatypes </li>
     <li> \ref Usd_Basic_Datatypes </li>
     <li> \ref Usd_Roles </li>
     <li> \ref Usd_Array_Datatypes </li>
     <li> \ref Usd_Dictionary_Type </li>
     </ol>
<li> \subpage Usd_Page_UTF_8 </li>
     <ol type="i">
     <li> \ref Usd_UTF_8_Overview </li>
     <li> \ref Usd_UTF_8_Encoding </li>
     <li> \ref Usd_UTF_8_Language_Support </li>
     <li> \ref Usd_UTF_8_Identifiers </li>
     <li> \ref Usd_UTF_8_Operation_Reference </li>
     <li> \ref Usd_UTF_8_Encoding_Reference </li>
     </ol>
<li> \subpage Usd_Page_PropertiesOfSceneDescription </li>
     <ol type="i">
     <li> \ref Usd_Ordering </li>
     <li> \ref Usd_ValueResolution </li>
     <li> \ref Usd_PrimSpecifiers </li>
     <li> \ref Usd_ModelHierarchy </li>
     <li> \ref Usd_ActiveInactive </li>
     <li> \ref Usd_Filetypes </li>
     <li> \ref Usd_AssetResolution </li>
     </ol>
<li> \subpage Usd_Page_AdvancedFeatures </li>
     <ol type="i">
     <li> \ref Usd_Page_DynamicFileFormat </li>
     <li> \ref Usd_Page_ScenegraphInstancing </li>
     <li> \ref Usd_Page_ValueClips </li>
     </ol>
<li> \subpage Usd_Page_AuthoringEditing </li>
     <ol type="i">
     <li> \ref Usd_SelectiveEditing </li>
     <li> \ref Usd_Notification </li>
     </ol>
<li> \subpage Usd_Page_CommonIdioms </li>
     <ol type="i">
     <li> \ref Usd_StageTraversal </li>
     <li> \ref Usd_WorkingWithSchemas </li>
     <li> \ref Usd_BoolReturns </li>
     <li> \ref Usd_ErrorReporting </li>
     </ol>
<li> \subpage Usd_Page_BestPractices </li>
     <ol type="i">
     <li> \ref Usd_SharedConstRef </li>
     <li> \ref Usd_DataStreaming </li>
     <li> \ref Usd_Payloads </li>
     </ol>
<li> \subpage Usd_Page_MultiThreading </li>
     <ol type="i">
     <li> \ref Usd_ThreadSafetyModel </li>
     <li> \ref Usd_InternalMultiThreading </li>
     </ol>
<li> \subpage Usd_Page_GeneratingSchemas </li>
     <ol type="i">
     <li> \ref Usd_IsAVsAPISchemas </li>
     <li> \ref Usd_SchemaExtensionPhilosophy </li>
     </ol>
</ol>
</td>

<td> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </td>


<td style="vertical-align: top;">
\n UsdStage owns the scenegraph and provides access to a composition.
\n UsdPrim is the hierarchically nestable unit of scene description.
\n UsdAttribute records time-varying data on prims.
\n UsdRelationship records links to other prims and properties.
\n UsdEditTarget allows editing of any layer/variation contained in a stage.
\n UsdNotice contains notifications that Usd issues when a stage's contents change.
\n UsdSchemaBase is the base class for generated schema classes.
\n UsdTimeCode is an ordinate that can be floating-point or an unvarying 'default'.
</td>

</tr>
</table>


